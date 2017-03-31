# __main__.py
#
# Copyright (C) 2017 Emilio Cabrera
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from time import sleep
import threading
import curses
import psutil

stop = False
cpu_num = psutil.cpu_count(logical=False)
cpu_load = ()
cpu_stats = {}
mem_stats = ()
swp_stats = ()
uptime = ()
p_stats = []
show = ('cpu_load', 'mem_stats', 'swp_stats', 'cpu_stats', 'processes')
mutexes = {}
for j in show:
    mutexes[j] = threading.Semaphore(1)


def bytes2human(n):
    """
    Taken from http://code.activestate.com/recipes/578019
    >>> bytes2human(10000)
    '9.8K'
    >>> bytes2human(100001221)
    '95.4M'  
    Args:
        n (int) 
    Returns:
        str
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def get_mem_usage():
    global mem_stats
    while not stop:
        mutexes['mem_stats'].acquire()
        mem_stats = (
            bytes2human(psutil.virtual_memory().total),
            bytes2human(psutil.virtual_memory().used),
            psutil.virtual_memory().percent
        )
        mutexes['mem_stats'].release()
        sleep(0.1)


def get_swp_usage():
    global swp_stats
    while not stop:
        mutexes['swp_stats'].acquire()
        swp_stats = (
            bytes2human(psutil.swap_memory().total),
            bytes2human(psutil.swap_memory().used),
            psutil.swap_memory().percent
        )
        mutexes['swp_stats'].release()
        sleep(0.1)


def get_cpu_stats():
    global cpu_stats
    while not stop:
        # for time in psutil.cpu_times_percent(percpu=True):
        #     times.append((time.user, time.system, time.idle))
        time = psutil.cpu_times_percent(percpu=False)
        freqs = []
        times = {
            'User': time.user,
            'System': time.system,
            'Idle': time.idle
        }
        for freq in psutil.cpu_freq(percpu=True):
            freqs.append(freq.current)
        mutexes['cpu_stats'].acquire()
        cpu_stats = {
            'time': times,
            'freq': freqs
        }
        mutexes['cpu_stats'].release()
        sleep(0.1)


def get_cpu_load():
    global cpu_load
    while not stop:
        mutexes['cpu_load'].acquire()
        cpu_load = psutil.cpu_percent(percpu=True)
        mutexes['cpu_load'].release()
        sleep(0.1)


def get_process_stats():
    global p_stats
    while not stop:
        p_stats = []
        mutexes['processes'].acquire()
        for process in psutil.process_iter():
            p_stats.append(process.as_dict(['pid', 'username', 'status',
                                            'memory_percent', 'cpu_percent',
                                            'name']))
        p_stats = sorted(p_stats, key=lambda p: p['cpu_percent'], reverse=True)
        mutexes['processes'].release()
        sleep(0.1)


def draw():
    global win

    def usage_bar(percent, before="", after=""):
        bar = "%s [%s] %s"
        size = win.getmaxyx()[1] - 7 - len(before) - len(after)
        bars = '|' * int(float(percent) / 100 * size)
        spaces = ' ' * (size - len(bars))
        return bar % (before, bars + spaces, after)

    linenum = 0

    if 'cpu_load' in show:
        mutexes['cpu_load'].acquire()
        for cpu in range(cpu_num):
            percent = cpu_load[cpu]
            before = 'CPU%s' % str(cpu + 1)
            after = '%04.1f%%' % percent
            win.addstr(linenum, 1, usage_bar(percent, before, after))
            linenum += 1
        mutexes['cpu_load'].release()
    if 'mem_stats' in show:
        before = 'RAM '
        mutexes['mem_stats'].acquire()
        total = mem_stats[0]
        used = mem_stats[1]
        percent = mem_stats[2]
        mutexes['mem_stats'].release()
        after = '%4s / %4s' % (used, total)
        win.addstr(linenum, 1, usage_bar(percent, before, after))
        linenum += 1
    if 'swp_stats' in show:
        before = 'SWAP'
        mutexes['swp_stats'].acquire()
        total = swp_stats[0]
        used = swp_stats[1]
        percent = swp_stats[2]
        mutexes['swp_stats'].release()
        after = '%4s / %4s' % (used, total)
        win.addstr(linenum, 1, usage_bar(percent, before, after))
        linenum += 1
    if 'cpu_stats' in show:
        size = int((win.getmaxyx()[1] - 6) / 5)
        mutexes['cpu_stats'].acquire()
        times = cpu_stats['time']
        freqs = cpu_stats['freq']
        mutexes['cpu_stats'].release()
        i = 1
        for n in times:
            win.addstr(linenum, i, "%s: %04.1f%%" % (n, times[n]))
            i += size
        for n in range(len(freqs)):
            win.addstr(linenum, i, "CPU%s: %03.1f GHz" % (n, freqs[n] / 1000))
            i += size
        linenum += 1
    if 'processes' in show:
        lformat = '%-6s %-10s %-8s %-5s %-5s %s'
        line = lformat % ('PID', 'USER', 'STATUS', 'CPU%', 'MEM%', 'NAME')
        win.addstr(linenum, 1, line + " " * (win.getmaxyx()[1] - len(line) - 3),
                   curses.A_REVERSE)
        linenum += 1
        lformat = '%-6s %-10s %-8s %05.1f %05.1f %s'

        mutexes['processes'].acquire()
        for i in range(win.getmaxyx()[0] - linenum - 1):
            win.addstr(linenum, 1, lformat % (p_stats[i]['pid'],
                                              p_stats[i]['username'],
                                              p_stats[i]['status'],
                                              p_stats[i]['cpu_percent'],
                                              p_stats[i]['memory_percent'],
                                              p_stats[i]['name'],
                                              ))
            win.clrtoeol()
            linenum += 1
        mutexes['processes'].release()
    win.refresh()

threads = [
    threading.Thread(target=get_cpu_load, args=[]),
    threading.Thread(target=get_cpu_stats, args=[]),
    threading.Thread(target=get_swp_usage, args=[]),
    threading.Thread(target=get_mem_usage, args=[]),
    threading.Thread(target=get_process_stats, args=[]),
]


def main(stdscr):
    global win
    win = stdscr
    for thread in threads:
        thread.start()
    while True:
        sleep(1)
        draw()


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except (KeyboardInterrupt, SystemExit):
        stop = True
        for thread in threads:
            thread.join()

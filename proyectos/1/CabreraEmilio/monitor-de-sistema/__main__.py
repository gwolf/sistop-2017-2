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

cpu_num = psutil.cpu_count()
cpu_load = []
cpu_time = []
mem_stats = []
swp_stats = []
uptime = []
process_stats = []
processes = []
show = ['cpu_load', 'mem_stats', 'swp_stats', 'processes']

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
    mem_stats = [
        bytes2human(psutil.virtual_memory().total),
        bytes2human(psutil.virtual_memory().used),
        psutil.virtual_memory().percent
    ]


def get_swp_usage():
    global swp_stats
    swp_stats = [
        bytes2human(psutil.swap_memory().total),
        bytes2human(psutil.swap_memory().used),
        psutil.swap_memory().percent
    ]


def get_cpu_time():
    global cpu_time
    for time in psutil.cpu_times(percpu=True):
        cpu_time = [time.user, time.system, time.idle]


def get_cpu_load():
    global cpu_load
    cpu_load = psutil.cpu_percent(percpu=True)


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
        for cpu in range(cpu_num):
            percent = cpu_load[cpu]
            before = 'CPU%s' % str(cpu + 1)
            after = '%04.1f%%' % percent
            win.addstr(linenum, 1, usage_bar(percent, before, after))
            linenum += 1
    if 'mem_stats' in show:
        before = 'RAM '
        total = mem_stats[0]
        used = mem_stats[1]
        percent = mem_stats[2]
        after = '%4s / %4s' % (used, total)
        win.addstr(linenum, 1, usage_bar(percent, before, after))
        linenum += 1
    if 'swp_stats' in show:
        before = 'SWAP'
        total = swp_stats[0]
        used = swp_stats[1]
        percent = swp_stats[2]
        after = '%4s / %4s' % (used, total)
        win.addstr(linenum, 1, usage_bar(percent, before, after))
        linenum += 1
    win.refresh()


def main(stdscr):
    global win
    win = stdscr
    while True:
        get_cpu_load()
        get_cpu_time()
        get_swp_usage()
        get_mem_usage()
        draw()
        sleep(1)


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except (KeyboardInterrupt, SystemExit):
        pass

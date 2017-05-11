#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import *
from time import sleep
import threading
import psutil

cpu_num = psutil.cpu_count(logical=False)
barcpu = []
lblCPU = []

def bytes2human(n):
    """
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

def get_carga_cpu():
    carga_cpu = ()
    carga_cpu = psutil.cpu_percent(percpu=True)
    for cpu in range(cpu_num):
        cpuStr[cpu].set('CPU%i %04.1f%%'%(cpu+1, carga_cpu[cpu]))
        barcpu[cpu]['value'] = int(float(carga_cpu[cpu]) / 100 * barcpu[cpu]['maximum'])
    get_usd_mem()
    tab2.after(1000, get_carga_cpu)

def get_stads_proc():
    tiempo = psutil.cpu_times_percent(percpu=False)
    freqs = []
    tiempos = {
        'Usuario': tiempo.user,
        'Sistema': tiempo.system,
        'Inactivo': tiempo.idle
    }
    for stad in tiempos:
        variable.set(variable.get() + '\t %s: %04.1f%%' % (stad, tiempos[stad]))
    
    for freq in psutil.cpu_freq(percpu=True):
        freqs.append(freq.current)
    for i in range(len(freqs)):
        variable.set(variable.get() + '\tCPU%s: %03.1f GHz' % (i, freqs[i] / 1000))

def get_usd_mem():
    usado = bytes2human(psutil.virtual_memory().used)
    total = bytes2human(psutil.virtual_memory().total)
    porciento = psutil.virtual_memory().percent
    ramStr.set('RAM %4s / %4s' %(usado, total))
    barRam['value'] = int(float(porciento) / 100 * barRam['maximum'])
    get_usd_vmem()


def get_usd_vmem():
    usado = bytes2human(psutil.swap_memory().used)
    total = bytes2human(psutil.swap_memory().total)
    porciento = psutil.swap_memory().percent
    vramStr.set('SWAP %4s / %4s' %(usado, total))
    barVram['value'] = int(float(porciento) / 100 * barRam['maximum'])


def get_procesos():
    stad_procesos = []
    stad_procesos = list(psutil.process_iter())
    for p in stad_procesos:
        try:
            p._name = p.name()
            p._pid = p.ppid()
            try:
                    p._username = p.username()
            except:
                    p._username = '?'
            p._cpu = p.cpu_percent(interval=0)
            p._ram = '%04.1f'%p.memory_percent()
            p._status = p.status()
        except psutil.NoSuchProcess:
            stad_procesos.remove(p)
        num_procs = len(psutil.pids())
        variable.set(str(num_procs) + ' Procesos en ejecución')
        get_stads_proc()
        treeProcesos.insert('', 'end', text=p._name,
                                    values=(p._pid,
                                            p._username,
                                            p._cpu,
                                            p._ram,
                                            p._status))

    tab1.after(2000, clear_procesos)

def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, command=lambda: \
               treeview_sort_column(tv, col, not reverse))

def clear_procesos():
    x = treeProcesos.get_children()
    if x != '()':
        for child in x:
            treeProcesos.delete(child)
    get_procesos()


def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, command=lambda: \
               treeview_sort_column(tv, col, not reverse))

# def main():
    # thr_cpu_ld = threading.Thread(target=get_carga_cpu)
    # thr_cpu_ld.start()
    # thr_cpu_st = threading.Thread(target=get_stad_cpu)
    # thr_cpu_st.start()
    # thr_swp_us =  threading.Thread(target=get_usd_vmem)
    # thr_swp_us.start()
    # thr_mem_us =  threading.Thread(target=get_usd_mem)
    # thr_mem_us.start()
    # thr_prc = threading.Thread(target=get_procesos)
    # thr_prc.start()

    # while 1:
    #     sleep(.5)
    #     get_stad_cpu()


ventana = Tk()
ventana.title("Proyecto 1: Monitor de SO")
ventana.geometry("715x600+0+0")
img = tk.Image("photo", file="system-monitor.png")
ventana.tk.call('wm','iconphoto',ventana._w,img)

note = ttk.Notebook(ventana, height=25)

tab1 = Frame(note)
tab2 = Frame(note)

note.add(tab1, text="Procesos")
note.add(tab2, text="Máquina")

"""Tab 1
Todo lo perteneciente a la pestaña 1,
aqui se encuentra la lista de procesos, su  pid,
el usuario que lo lanza, el porcentaje de cpu, el porcentaje de ram y
el estado del proceso.
"""
treeProcesos = ttk.Treeview(tab1)

treeProcesos["columns"] = ("PId", "Usuario", "CPU", "Memoria", "Estado")

scrollProcesos = ttk.Scrollbar(tab1)
scrollProcesos.pack(side=RIGHT, fill=Y)

treeProcesos['yscrollcommand'] = scrollProcesos.set
treeProcesos.column("PId", width=100)
treeProcesos.column("Usuario", width=120)
treeProcesos.column("CPU", width=90)
treeProcesos.column("Memoria", width=90)
treeProcesos.column("Estado", width=72)
treeProcesos.heading("PId", text="PId", command=lambda: \
                     treeview_sort_column(treeProcesos, "PId", False))
treeProcesos.heading("Usuario", text="Usuario", command=lambda: \
                     treeview_sort_column(treeProcesos, "Usuario", False))
treeProcesos.heading("CPU", text="% CPU", command=lambda: \
                     treeview_sort_column(treeProcesos, "CPU", False))
treeProcesos.heading("Memoria", text="% Memoria", command=lambda: \
                     treeview_sort_column(treeProcesos, "Memoria", False))
treeProcesos.heading("Estado", text="Estado", command=lambda: \
                     treeview_sort_column(treeProcesos, "Estado", False))

variable = StringVar()
lblstatus = Label(ventana, bd=1, state=ACTIVE, relief=SUNKEN, anchor=W,
                  textvariable=variable,
                  font=('arial', 9, 'normal'))

user = StringVar()
lbluser = Label(ventana, bd=1, state=ACTIVE, relief=SUNKEN, anchor=W,
                  textvariable=user,
                  font=('arial', 9, 'normal'))

"""Tab 2
Aqui se muestran barras con las estadisticas de uso de la máquina.
"""
# leftResumen = Frame(tab2)
# leftResumen.pack(side=LEFT, fill=Y)
# rightResumen = Frame(tab2)
# rightResumen.pack(side=RIGHT, fill=X)

cpuStr = []
ramStr = StringVar()
vramStr = StringVar()

lblRam = Label(tab2, bd=1, state=ACTIVE, anchor=W,
                  textvariable=ramStr,
                  font=('arial', 11, 'normal'))

lblVram = Label(tab2, bd=1, state=ACTIVE, anchor=W,
                  textvariable=vramStr,
                  font=('arial', 11, 'normal'))

lblRam.grid(row=cpu_num+1)
lblVram.grid(row=cpu_num+2)

for cpu in range(cpu_num):
    cpuStr.append(StringVar())
    lblCPU.append(Label(tab2, bd=1, state=ACTIVE, anchor=W,
                  textvariable=cpuStr[cpu],
                  font=('arial', 15, 'normal')))
    barcpu.append(ttk.Progressbar(tab2, orient="horizontal", length=200, mode="determinate"))
    barcpu[cpu]['maximum'] = 1000
    lblCPU[cpu].grid(row = cpu, sticky=E)
    barcpu[cpu].grid(row = cpu, column = 1, sticky = (E,W),padx=5)

barRam = ttk.Progressbar(tab2, orient="horizontal", length=200, mode="determinate")
barRam['maximum'] = 1000
barRam.grid(row=cpu_num+1, column = 1, sticky = (E,W),padx=5)

barVram = ttk.Progressbar(tab2, orient="horizontal", length=200, mode="determinate")
barVram['maximum'] = 1000
barVram.grid(row=cpu_num+2, column = 1, sticky = (E,W),padx=5)

"""Pack 
Algunas cosa necesarias para la creacion
de la ventana, las tablas, los textos y las barras.
"""
# listCargas.pack(side=LEFT, fill=Y)
lblstatus.pack(side=BOTTOM, fill=X)
treeProcesos.pack(side=LEFT, fill=BOTH, expand=1)
note.pack(side=LEFT, fill=BOTH, expand=1)
scrollProcesos.config(command=treeProcesos.yview)
tab1.after(200, clear_procesos)
tab2.after(200, get_carga_cpu)
ventana.mainloop()

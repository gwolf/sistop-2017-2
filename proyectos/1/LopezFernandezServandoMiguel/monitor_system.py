#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from gathering_information import Processes, Processor, Memory
from time import sleep
from threading import Thread, Semaphore
from subprocess import call

GObject.threads_init()

class MainWindow():

	def __init__(self):


		#Create window
		self.builder = Gtk.Builder()
		self.builder.add_from_file("main_window1.glade")


		self.gtk_list = Gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str)
		self.g = 0
		self.sl = ''
		
		#Get objects
		self.get_objects()

		self.connect_events()


		self.processes = Processes()
		self.processor = Processor()
		self.memory = Memory()

		
		self.create_tree()
		self.generate_cpu_info()
		self.generate_memory_info()

		
		self.window.show_all()
		Gtk.main()

	def get_objects(self):
		self.window = self.builder.get_object('MainWindow')
		self.processes_tree = self.builder.get_object('treeview_process')
		self.switch = self.builder.get_object('switch_update')
		self.entry3_process_id = self.builder.get_object('entry3_process_id')
		self.entry3_process_signal = self.builder.get_object('entry3_process_signal')
		self.kill_button = self.builder.get_object('button3_process')
		self.searchentry = self.builder.get_object('searchentry1')
		self.main_notebook = self.builder.get_object('main_notebook')
		self.levelbar_cpu_usage = self.builder.get_object('levelbar_cpu_usage')
		self.label_cpu_usage = self.builder.get_object('label_cpu_usage')
		self.label_model = self.builder.get_object('label_model')
		self.image_model = self.builder.get_object('image_model')
		self.label_clock_speed = self.builder.get_object('label_clock_speed')
		self.label_cpu_cores = self.builder.get_object('label_cpu_cores')
		self.notebook_resources = self.builder.get_object('notebook_resources')

		self.levelbar_total = self.builder.get_object('levelbar_total')
		self.label_totat = self.builder.get_object('label_totat')
		self.levelbar_available = self.builder.get_object('levelbar_available')
		self.label_available = self.builder.get_object('label_available')
		self.levelbar_used = self.builder.get_object('levelbar_used')
		self.label_used = self.builder.get_object('label_used')
		self.levelbar_free = self.builder.get_object('levelbar_free')
		self.label_free = self.builder.get_object('label_free')





	def connect_events(self):
		self.kill_button.connect('clicked', self.kill_action)		
		#self.searchentry.connect('search-changed', self.to_filter )
		self.window.connect('delete-event', Gtk.main_quit)

	# funcio que actualiza la interfaz grafica
	def activo(self):
		
		if self.switch.get_state():
			if self.main_notebook.get_current_page() == 0 :
				self.sl = self.entry3_process_id.get_text()
				self.update_tree()
			elif self.main_notebook.get_current_page() == 1 :
				if self.notebook_resources.get_current_page() == 0:
					self.update_cpu_info()
				elif self.notebook_resources.get_current_page() == 1:
					self.update_memory()

		return True


	def kill_action(self, widget):

		texto_of_signal = self.entry3_process_signal.get_text()
		texto_of_pid = self.entry3_process_id.get_text()

		if (texto_of_signal == '' and texto_of_pid == '') or texto_of_pid == '':
			pass
		elif texto_of_signal == '':
			call(['kill','-9',texto_of_pid])
		elif texto_of_signal != '':
			texto_of_signal = '-'+texto_of_signal
			call(['kill', texto_of_signal,texto_of_pid])

		
	def create_tree(self):
		
		render = Gtk.CellRendererText()
		
		self.processes.pull_processes_list()
		for e in self.processes.get_list_processes():
			self.gtk_list.append(e)

		
		self.processes_tree.set_model(self.gtk_list)
		
		for i, title in self.processes.columns_name:
			column = Gtk.TreeViewColumn(title, render, text=i)

			column.set_sort_column_id(i)
			self.processes_tree.append_column(column)
		


		select = self.processes_tree.get_selection()
		select.connect("changed", self.on_tree_selection_changed)


		self.g = GObject.timeout_add(3000, self.activo)

	def generate_cpu_info(self):

		self.levelbar_cpu_usage.set_max_value(100.0)
		self.levelbar_cpu_usage.set_min_value(0.0)
		
		Thread(target=self.processes.pull_processes_list, args=[]).start()
		Thread(target=self.processor.measure_cpu_usage, args=[self.processes.get_list_processes()]).start()
		self.label_clock_speed.set_text(self.processor.cpu_speed)
		f = self.processor.cpu_family
		self.label_model.set_text(f)
		
		if 'inte' in f.lower():
			self.image_model.set_from_file('intel.png')
		else:
			self.image_model.set_from_file('amd.png')

		self.label_cpu_cores.set_text(self.processor.cpu_cores)

		self.levelbar_cpu_usage.set_value(self.processor.get_average())
		
		self.label_cpu_usage.set_text(self.processor.cpu_usage+'%')

	def generate_memory_info(self):

		self.memory.pull_mem_stats()
		
		self.levelbar_total.set_max_value(self.memory.tot_mem)
		self.levelbar_total.set_min_value(0.0)
		self.label_totat.set_text(self.memory.get_total())
		self.levelbar_total.set_value(self.memory.tot_mem)
		
		
		self.levelbar_available.set_max_value(self.memory.tot_mem)
		self.levelbar_available.set_min_value(0.0)
		self.levelbar_available.set_value(self.memory.available_mem)
		self.levelbar_available.set_inverted(True)
		self.label_available.set_text(self.memory.get_porcent_available())
		
		self.levelbar_used.set_max_value(self.memory.tot_mem)
		self.levelbar_used.set_min_value(0.0)
		self.levelbar_used.set_value(self.memory.used_mem)
		self.label_used.set_text(self.memory.get_porcent_used())

		self.levelbar_free.set_max_value(self.memory.tot_mem)
		self.levelbar_free.set_min_value(0.0)
		self.levelbar_free.set_value(self.memory.free_mem)
		self.levelbar_free.set_inverted(True)
		self.label_free.set_text(self.memory.get_porcent_free())

	def update_memory(self):
		Thread( target=self.memory.pull_mem_stats, args=[] ).start()

		self.label_totat.set_text(self.memory.get_total())
		self.levelbar_total.set_value(self.memory.tot_mem)

		self.levelbar_available.set_value(self.memory.available_mem)
		self.label_available.set_text(self.memory.get_porcent_available())

		self.levelbar_used.set_value(self.memory.used_mem)
		self.label_used.set_text(self.memory.get_porcent_used())

		self.levelbar_free.set_value(self.memory.free_mem)
		self.label_free.set_text(self.memory.get_porcent_free())


	# revisa si se selecciono algo en los procesos , si asi es pone el process id en la 
	# text box 
	def on_tree_selection_changed(self, selection):
		model, treeiter = selection.get_selected()
		if treeiter != None:
			#print("You selected : ", model[treeiter][1])
			self.entry3_process_id.set_text(model[treeiter][1])

	def update_cpu_info(self):
		Thread(target=self.processes.pull_processes_list() , args=[]).start()
		Thread(target=self.processor.measure_cpu_usage, args=[self.processes.get_list_processes()]).start()
		Thread(target=self.processor.get_cpu_info , args=[]).start()

		self.label_clock_speed.set_text(self.processor.cpu_speed)
		self.label_cpu_cores.set_text(self.processor.cpu_cores)
		self.levelbar_cpu_usage.set_value(self.processor.get_average())
		#self.levelbar_cpu_usage.set_value(self.processor.measure_cpu_usage(self.processes.list_processes))
		
		self.label_cpu_usage.set_text(self.processor.cpu_usage+'%')



	def update_tree(self):
		
		Thread(target=self.processes.pull_processes_list, args=[]).start()
		self.gtk_list.clear()

		render = Gtk.CellRendererText()

		#self.processes.pull_processes_list()
		for e in self.processes.get_list_processes():
			self.gtk_list.append(e)

		
		self.processes_tree.set_model(self.gtk_list)
		for i, title in self.processes.columns_name:
			column = Gtk.TreeViewColumn(title, render, text=i)

			column.set_sort_column_id(i)
			self.processes_tree.append_column(column)
		self.entry3_process_id.set_text(self.sl)



# punto de entrada al programa
if __name__ == '__main__':
	w = MainWindow()
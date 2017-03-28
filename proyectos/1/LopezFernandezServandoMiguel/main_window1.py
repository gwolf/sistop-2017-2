#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from gathering_information import Processes
from time import sleep
from threading import Thread

#GObject.threads_init()

class MainWindow():

	def __init__(self):


		#Create window
		builder = Gtk.Builder()
		builder.add_from_file("main_window1.glade")			

		self.gtk_list = Gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str)
		self.g = 0
		
		#Get objects
		self.window = builder.get_object('MainWindow')
		self.processes_tree = builder.get_object('treeview_process')
		self.processes = Processes()

		self.switch = builder.get_object('switch_update')
		
		

		
		self.create_tree()

		self.window.connect('delete-event', Gtk.main_quit)
		self.window.show_all()
		Gtk.main()

	def activo(self):
		while self.switch.get_state():
			print('Activo')
			self.update_tree()
		#else:
		#	print('Desactivado')
		return False
		
	def create_tree(self):
		
		render = Gtk.CellRendererText()

		Thread(target=self.processes.get_list_processes, args=[]).start()
		print(self.processes.list_processes)
		sleep(3)
		
		#for e in self.processes.get_list_processes():
		for e in self.processes.get_list():
			self.gtk_list.append(e)

		#print(self.processes.get_list_processes())
		self.processes_tree.set_model(self.gtk_list)
		for i, title in self.processes.columns_name:
			column = Gtk.TreeViewColumn(title, render, text=i)

			column.set_sort_column_id(i)
			self.processes_tree.append_column(column)
		self.g = GObject.timeout_add(1000, self.update_tree, self)
		

	def update_tree(self, widget):
		
		self.gtk_list.clear()

		#render = Gtk.CellRendererText()
		Thread(target=self.processes.get_list_processes, args=[]).start()

		for e in self.processes.get_list():
			self.gtk_list.append(e)

		#print(self.processes.get_list_processes())
		self.processes_tree.set_model(self.gtk_list)
		#for i, title in self.processes.columns_name:
		#	column = Gtk.TreeViewColumn(title, render, text=i)

		#	column.set_sort_column_id(i)
		#	self.processes_tree.append_column(column)

		return False


	
if __name__ == '__main__':
	w = MainWindow()
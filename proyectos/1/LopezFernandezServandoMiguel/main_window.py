#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gathering_information import Processes

class MainWindow():

	def __init__(self):

		builder = Gtk.Builder()
		builder.add_from_file("main_window.glade")	

		self.processes = Processes()

		self.window = builder.get_object('MainWindow')
		self.processes_tree = builder.get_object('processes_tree')
		
		
		self.update_tree()
		self.window.connect('delete-event', Gtk.main_quit)
		self.window.show_all()
		Gtk.main()

	def update_tree(self):

		gtk_list = Gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str)
		
		render = Gtk.CellRendererText()
	
		for e in self.processes.get_list_processes():
			gtk_list.append(e)

		print(self.processes.get_list_processes())
		self.processes_tree.set_model(gtk_list)
		for i, title in self.processes.columns_name:
			self.processes_tree.append_column(Gtk.TreeViewColumn(title, render, text=i))


		
		
if __name__ == '__main__':
	w = MainWindow()
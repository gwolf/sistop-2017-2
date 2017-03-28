from subprocess import call, getoutput
from threading import Semaphore

class Processes():

	names = ['USER', 'PID', '%CPU', r'%MEM', 'VCZ', 'RSS', 'TTY', 'STAT', 'START', 'TIME', 'COMMAND']

	def __init__(self):
		self.list_processes = []
		self.columns_name = enumerate(Processes.names)
		self.signal = Semaphore(0)
		self.mutex = Semaphore(1)


	def pull_processes_list(self):
		self.list_processes = []
		first_line = True
		with open('data.txt', mode='w') as fl:
			call(['ps','aux'], stdout=fl)
		
		self.mutex.acquire()
		with open('data.txt', mode='r') as fl:
			for line in fl:
				if not first_line:
					self.list_processes.append(line.strip().split(None, 10))
				else:
					first_line = False
		self.mutex.release()
		

		self.signal.release()


	def get_list_processes(self):
		self.signal.acquire()
		return self.list_processes
		


class Memory():

	def __init__(self):
		self.tot_mem = 0
		self.free_mem = 0
		self.used_mem = 0

	def pull_mem_stats(self):
		self.tot_mem = float(getoutput('grep MemTotal /proc/meminfo').split()[1])
		self.free_mem = float(getoutput('grep MemTotal /proc/meminfo').split()[1])
		self.used_mem = self.tot_mem - self.free_mem

	def get_tot_mem(self):
		return self.tot_mem

	def get_free_mem(self):
		return self.free_mem

	def get_average_used_mem(self):
		return (self.used_mem*100)/self.tot_mem


class Processor():

	def __init__(self):
		self.cpu_family = ''
		self.cpu_cores = ''
		self.cpu_speed = ''
		self.cpu_usage = ''
		#self.cpu_temp = ''

	def measure_cpu_usage(self, l):
		average = 0.0
		for line in fl:
			average += float(line.split()[2])
		return average

	def get_cpu_info(self):
		with open('/proc/cpuinfo', mode='r', encoding='utf-8') as file:
			for line in file:
				if 'model name' in line:
					self.cpu_family = line.split('')[2]
				elif 'cpu MHz' in line:
					self.cpu_speed = line.split('')[2]
				elif 'cpu MHz' in line:
					self.cpu_cores = line.split('')[2]





if __name__ == '__main__':
	p = Processes()
	p.pull_processes_list()
	print(p.get_list_processes()[0])



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
		self.signal.release()


		self.mutex.release()


	def get_list_processes(self):
		self.signal.acquire()
		return self.list_processes
		


class Memory():

	def __init__(self):
		self.tot_mem = 0
		self.free_mem = 0
		self.used_mem = 0
		self.mutex = Semaphore(1)
		self.signal = Semaphore(0)

	def pull_mem_stats(self):
		self.mutex.acquire()
		
		self.tot_mem = float(getoutput('grep MemTotal /proc/meminfo').split(None)[1])
		self.free_mem = float(getoutput('grep MemFree /proc/meminfo').split(None)[1])
		self.available_mem = float(getoutput('grep MemAvailable /proc/meminfo').split(None)[1])
		self.used_mem = self.tot_mem - self.free_mem
		self.signal.release()
		self.mutex.release()

	def get_total(self):
		self.signal.acquire()
		return '{}'.format(self.human_size(self.tot_mem))
		

	def get_porcent_free(self):
		s = ''
		p = (self.free_mem * 100) / self.tot_mem
		s = '{}    {:.2f}%'.format(self.human_size(self.free_mem), p)
		return s


	def get_porcent_used(self):
		s = ''
		p = (self.used_mem * 100) / self.tot_mem
		s = '{}    {:.2f}%'.format(self.human_size(self.used_mem), p)
		return s


	def get_porcent_available(self):
		s = ''
		p = (self.available_mem * 100) / self.tot_mem
		s = '{}    {:.2f}%'.format(self.human_size(self.available_mem), p)
		return s

	def human_size(self, size):
		SUFFIXES = [ 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']

		for e in SUFFIXES:
			size /= 1024
			if size < 1024:
				return '{0:.1f} {1}'.format(size, e)



class Processor():

	def __init__(self):
	
		self.cpu_family = ''
		self.cpu_cores = ''
		self.cpu_speed = ''
		self.cpu_usage = ''
		self.average = 0.0
		self.mutex = Semaphore(1)
		self.mutex1 = Semaphore(1)
		self.signal = Semaphore(0)
		#self.cpu_temp = ''
		self.get_cpu_info()
		

	def measure_cpu_usage(self, process_list):
		self.average = 0.0
		
		self.mutex.acquire()

		for e in process_list:
			self.average += float(e[2])
			self.cpu_usage = '{0:.2f}'.format(self.average)
	
		self.signal.release()
		self.mutex.release()
		return self.average

	def get_cpu_info(self):
		
		
		self.mutex1.acquire()
		with open('/proc/cpuinfo', mode='r', encoding='utf-8') as file:

			for line in file:
				if 'model name' in line:
					self.cpu_family = line.split(' ',2)[2]
				elif 'cpu MHz' in line:
					self.cpu_speed = line.split(' ')[2]
				elif 'cpu cores' in line:
					self.cpu_cores = line.split(' ')[2]
		self.mutex1.release()

	def get_average(self):
		self.signal.acquire()
		return self.average




if __name__ == '__main__':
	p = Processes()
	p.pull_processes_list()
	print(p.get_list_processes()[0])



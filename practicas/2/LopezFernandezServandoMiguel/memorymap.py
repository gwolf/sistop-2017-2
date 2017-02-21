from os import system

def memorySize(bts):
	scales = ['KB','MB','GB', 'TB']
	for scale in scales:
		bts /= 1024;
		if bts < 1024:
			return '{:.3f} {}'.format(bts,scale)

def memoryMap():
	data = list()
	size = int()
	system('less /proc/iomem > data.txt')
	with open('data.txt') as fl:
		data = [line for line in fl]
	with open('data.txt',mode='w') as fl:
		for line in data:
			(mem, name) = line.split(' : ')
			name = name.replace('\n','') if '\n' in name else name
			(low, hi) = mem.split('-')
			size = memorySize(int(hi, 16) - int(low, 16))
			fl.write(' {} - {}   {}  --> {}\n'.format(low.strip(), hi.strip(), size, name))

if __name__ == '__main__':
	memoryMap()

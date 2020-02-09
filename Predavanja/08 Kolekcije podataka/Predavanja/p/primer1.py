import copy

def get_data():
	l = []
	while True:
		data = input('value: ')
		if data=='q':
			break
		try:
			data = float(data)
		except:
			continue
		l.append(data)
	return l

def mean(data):
	return sum(data)/len(data)

def median(data):
	data_c = copy.copy(data)
	data_c.sort()
	return data_c[int(len(data_c)/2)]

def std_dev(data, avg):
	sum_dev_sqr = 0
	for num in data:
		dev = avg - num
		sum_dev_sqr = sum_dev_sqr + dev * dev
	return sqrt(sum_dev_sqr/(len(data)-1))


def main():
	data = get_data()
	print(data)
	print(median(data))

main()


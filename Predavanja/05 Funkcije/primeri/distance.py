import math
def distance(x1,x2,y1,y2):
	return(math.sqrt((x1-y1)**2+(x2-y2)**2))
def main():
	print(distance(1,1,2,2))
main()
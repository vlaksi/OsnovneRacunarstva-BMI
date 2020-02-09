def racquetball():
	score_a=0
	score_b=0
	# a ima 15 ili b ima 15 ili neki od igraca ima 7 poena a drugi ima 0 poena
	# while not((score_a==15 or score_b==15) or (score_a==7 and score_b==0) or (score_a==0 and score_b==7)):
	# while (not(score_a==15 or score_b==15) and not(score_a==7 and score_b==0) and not(score_a==0 and score_b==7)):
	while (not(score_a==15) and not(score_b==15)) and (not(score_a==7) or not(score_b==0)) and (not(score_a==0) or not(score_b==7)):
		point = input("point: ")
		if point=="a":
			score_a+=1
		elif point=="b":
			score_b+=1
		print("A: ",score_a,"B: ",score_b)		
	print("final score: ")
	print("A: ",score_a,"B: ",score_b)		

def main():
	racquetball()

if __name__ == '__main__':
	main()
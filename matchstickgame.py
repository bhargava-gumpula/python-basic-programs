totalSticks = 21
userSticks = 0
while True:
	userSticks = int(input("how many sticks do you want to take (1 - 4)"))
	if userSticks > 4 or userSticks < 1:
		continue
	computerSticks = 5 - userSticks
	totalSticks = totalSticks - (computerSticks + userSticks)
	print("The Computer Chose %s Sticks" %computerSticks)
	print("There are %s sticks left" %totalSticks)	
	if totalSticks <= 1:
                print("You Lose")
                break

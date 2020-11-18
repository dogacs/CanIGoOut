import datetime
import sys

age = int(input("Yaşınızı girin: "))
time = datetime.datetime.now()
hour = time.hour
day = time.weekday()

if(day>4): #haftasonu
	if(hour >= 10 and hour < 20):
		if(age > 20 and age < 65):
			print("maskeni tak, çık")
			sys.exit()
		elif(age >= 65 and hour < 13):
			print("maskeni tak, çık")
			sys.exit()
		elif(age <= 20 and hour >= 13 and hour < 16):
			print("maskeni tak, çık")
			sys.exit()
							
	print("otur evinde")

else: #haftaiçi
	job = input("Çalışıyor musunuz(y/n)?: ")
	if job == "y":
		print("git çalış")
		sys.exit()
	elif job == "n":
		if(age > 20 and age < 65):
			print("maskeni tak, çık")
			sys.exit()
		elif(age >= 65 and hour >= 10 and hour < 13):
			print("maskeni tak, çık")
			sys.exit()
		elif(age <= 20 and hour >= 13 and hour < 16):
			print("maskeni tak, çık")
			sys.exit()

	print("otur evinde")

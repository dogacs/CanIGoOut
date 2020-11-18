import datetime
import sys

age = int(input("Yaşınızı girin: "))
time = datetime.datetime.now()
hour = time.hour
day = time.weekday()

if(day>5): #haftasonu
	if(hour >= 10):
		if(hour < 20):
			if(age > 20 and age < 65) | (hour <= 16):
				print("maskeni tak, çık")
				sys.exit()
							
	print("otur evinde")

else: #haftaiçi
	job = input("Çalışıyor musunuz(y/n)?: ")
	if job == "y":
		print("git çalış")
	else:
		print("maskeni tak, çık")

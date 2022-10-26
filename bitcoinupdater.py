import cryptocompare
import time
import os
import sys
##cryptocompare.cryptocompare._set_api_key_parameter(6e8cebd645566fda2804cffb4490a4ca21d63045c06784b8f48b243966fc0b39)


print("Choose Coin To See Live Price Of :)")
print("Available Coins, BTC, ETH")
option = input("Enter Coin: ")


if option == "BTC":
	print("Type Exit To Stop :)")
	while True:
		print(cryptocompare.get_price('BTC', currency='USD', full=False))
		exit = input()
		if exit == "Exit":
			sys.exit("Exiting")
		##exit = input("Type Exit To Stop: ")
		##if exit == "Exit":
			##os.execl(sys.executable, sys.executable, *sys.argv)
		time.sleep(5)

if option == "ETH":
	print("Type Exit To Stop :)")
	while True:
		print(cryptocompare.get_price('ETH', currency='USD', full=False))
		exit = input()
		if exit == "Exit":
			sys.exit("Exiting")
		##exit = input("Type Exit To Stop: ")
		##if exit == "Exit":
			##os.execl(sys.executable, sys.executable, *sys.argv)
		time.sleep(5)


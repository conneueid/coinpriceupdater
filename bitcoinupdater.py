import cryptocompare
import time
while True:
	print(cryptocompare.get_price('BTC', currency='USD', full=False))
	time.sleep(5)
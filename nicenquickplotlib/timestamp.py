import datetime
from time import sleep

def get_timestamp():
	"""
	Returns a numeric string with a timestamp. It also halts the execution 
	of the program during 10 micro seconds to ensure that all returned
	timestamps to be different and unique.
	
	Returns
	-------
	str
		String containing the timestamp. Format isYYYYMMDDHHMMSSmmmmmm.
	
	Example
	-------	
	>>> get_timestamp()
	'20181013234913378084'
	>>> [get_timestamp(), get_timestamp()]
	['20181013235501158401', '20181013235501158583']
	"""
	timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
	sleep(10e-6) # This ensures that there will not exist two equal timestamps.
	return timestamp


def data_type(n):
	#check if n is a list ,then do_something
	if isinstance(n, list):
		if len(n) < 3:
			return None
		else:
		    return n[2]

	elif type (n)== bool:
		return n
	#check if  n is int,then do something 
	elif isinstance(n, int):
		if n < 100:
			return "less to 100"
		else:
			n > 100 
			return "more than 100"

	#check if n is ,bool or str or no value
	elif type(n) == str:
		return len(n)
	else:
		return "no value"	

#print outcome
print(data_type(45))

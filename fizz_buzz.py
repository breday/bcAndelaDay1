def fizz_buzz(n):
		#check if n is divisible by 3 and 5,return FizzBuzz
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
        #check if nis divisible by 3,print Fizz
    elif n % 3 == 0:
        return 'Fizz'
        #check if n is divisible by 5,return Buzz
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n
        
#print result
print(fizz_buzz(8))


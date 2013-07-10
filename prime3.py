#module for calculating and accessing primes, etc.
from sys import getsizeof
from math import ceil, floor


#two is the first prime, given here as an example 
#and to aviod checking if these are empty
prime_list = [2]
ordinal_index = {2:1}


#all primes below this number have been found (inclusively)
latest_upto = 2

#used to change prime indexing behavior. TODO
index_policy = 0

#todo: optomize these number while being safe
MAX_SET_SIZE = 100000000000000

def prime_gen(upto):
    '''
    calculates the primes lower than upto (inclusively) 
    and stores them in prime_list. Returns None
    '''
    try:
        float(upto)
        assert upto > 0
    except:
        raise Exception
        
    global prime_list
    global latest_upto
    if upto > latest_upto:

        numset = set()
        while floor(upto) > latest_upto:
            startnum = latest_upto + 1
            numset.clear()
            
            #generate the set of next numbers 
            #as high as memory allows
            for num in range(startnum, min(int(upto+1), startnum**2)):
                if getsizeof(numset) > MAX_SET_SIZE:
                    break
                    
                numset.add(num)
            
            endnum = startnum+len(numset)-1
                
            #remove known primes
            for prime in prime_list:
                first_composite = max(ceil(startnum/prime)*prime, prime**2)
                numset -= set(range(first_composite, endnum+1, prime))
                
            prime_list.extend(numset)
            latest_upto = endnum
            
        prime_list.sort()

def latest_prime():
  '''
  returns largest prime calculated so far
  '''
  return prime_list[-1]
  
def nth_prime(n):
  '''
  returns the nth prime number (2 is the 1st prime, etc.)
  '''
  try:
    int(n)
    assert n >= 1
  except:
    raise Exception
      
  upto = 2*max(n, latest_upto)
  while len(prime_list) < n:
    prime_gen(upto)
    upto *= 10
  return prime_list[n-1]
  
  
def is_prime(integer):
  '''
  returns true if integer is prime
  '''
  if type(integer) != int or integer < 1:
    raise Exception
      
  if integer in ordinal_index:
    return True
    
  if integer > latest_upto:
    prime_gen(integer)
    return integer == latest_prime()
    
  i = index(integer)
  return integer == prime_list[i]
  
def get_ordinal(prime):
  '''
  returns the ordinal of a given prime (2 is the 1st prime, etc.)
  '''
  try:
    int(prime)
    assert prime >= 1
  except:
    raise Exception
  
  global ordinal_index
  if prime in ordinal_index:
    return ordinal_index[prime]
    
  if prime > latest_prime():
    prime_gen(prime)
    if latest_prime() != prime:
      raise Exception
    i = len(prime_list) -1
  else:
    i = index(prime)
    if prime_list[i] != prime:
        raise Exception
        
  ordinal = i + 1
  ordinal_index[prime] = ordinal
  return ordinal
  
def largest_under(number):
  '''
  returns the largest prime below number
  '''
  try:
    float(number)
    assert number > 2
  except:
    raise Exception

  if number in ordinal_index:
    return prime_list[ordinal_index[number]-1]
    
  if number > latest_upto:
    prime_gen(number-1)
    return latest_prime()
    
  i = index(number)
  if number == prime_list[i]:
    return prime_list[i-1]
  else:
    return prime_list[i]
  
def factorize(integer):
  '''
  returns a factorized form the number as a dictionary with 
  prime factors as keys and the exponents as values. 
  E.g. 12 would be {2:2, 3:1}. 
  Returns empty dictionaries for 1. 
  '''
  if type(integer) != int or integer < 1:
    raise Exception
    
  factors = dict()
  least_possible_factor = 2
  number = integer
  
  n = 1
  while n <= number//least_possible_factor:
    prime = nth_prime(n)
    if number%prime == 0:
        exponent = 0
        while number%prime == 0:
            number //= prime
            exponent += 1
            
        factors[prime] = exponent
        least_possible_factor = nth_prime(n+1)
        
    n += 1
    
  if number != 1:
    factors[number] = 1
    
  return factors
  
def combine(factors):
  '''
  returns and integer by reverses the factorize function.
  '''
  if type(factors) != dict:
    raise Exception
    
  total = 1
  for (prime, exponent) in factors.items():
    try:
      total *= prime**exponent
    except:
      raise Exception('Unexpected contents in factors')
    
  return total
  
def index(number):
    '''
    returns the index of number in the prime_list, 
    or the index of the prime below it
    '''
    try:
        float(number)
        assert number >= 2
        assert number <= latest_upto
    except:
        raise Exception
        
    def search(start, end):
        if start == end:
            return start
            
        middle = start + (end-start)//2
        if prime_list[middle] == number:
            return middle
            
        if prime_list[middle] < number:
            return search(middle+1, end)
        else:
            return search(start, middle)
            
    result = search(0, len(prime_list)-1)
    if prime_list[result] == number:
        return result
    else:
        return result-1
        
def reset():
    '''
    returns module variables to there initial state.
    Useful for testing
    '''
    global prime_list
    global ordinal_index
    global latest_upto
    
    prime_list = [2]
    ordinal_index = {2:1}
    latest_upto = 2
  
  
#module for calculating and accessing primes, etc.
from sys import getsizeof
from math import ceil


#two is the first prime, given here as an example 
#and to aviod checking if these are empty
prime_list = [2]
ordinal_index = {2:1}


#all primes below this number have been found (inclusively)
latest_upto = 2

#used to change prime indexing behavior
index_policy = 0

#todo: optomize these number while being safe
MAX_LIST_SIZE = 1000000
MAX_SET_SIZE = 100000000000000

def prime_gen(upto):
    '''
    calculates the primes lower than upto (inclusively) 
    and stores them in prime_list. Returns None
    '''
    if upto > latest_upto:
        global prime_list
        global latest_upto
        numset = set()
        while upto > latest_upto:
            startnum = latest_upto + 1
            numset.clear()
            
            #generate the set of next numbers 
            #as high as memory allows
            for num in range(startnum, min(upto+1, startnum**2)):
                if getsizeof(numset) > MAX_SET_SIZE:
                    print('length = {} and size {} bytes'.format(len(numset), getsizeof(numset)))
                    break
                numset.add(num)
            
            endnum = startnum+len(numset)-1
                
            #remove known primes
            for prime in prime_list:
                first_composite = max(ceil(startnum/prime)*prime, prime**2)
                numset -= set(range(first_composite, endnum+1, prime))
                
            global prime_list
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
  if type(n) != int:
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
  if type(integer) != int:
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
  global ordinal_index
  ordinal_index[prime] = ordinal
  return ordinal
  
def largest_under(number):
  '''
  returns the largest prime below number
  '''
  if number <= 2:
    raise Exception
  if number in ordinal_index:
    return prime_list[ordinal_index[number]-1]
  if number > latest_upto:
    prime_gen(number-1)
    return latest_prime()
  i = index(number)
  if number == prime_list[i]:
    return i-1
  else:
    return i
  
def factorize(int):
  '''
  returns a factorized form the number as a dictionary with 
  prime factors as keys and the exponents as values. 
  E.g. 12 would be {2:2, 3:1}. 
  Returns empty dictionaries for 1. 
  '''
  None
  
def combine(factors):
  '''
  returns and integer by reverses the factorize function, 
  '''
  if type(factors) != dict:
    raise Exception
  total = 0
  for (prime, exponent) in factors.items():
    total += prime**exponent
  return total
  
def index(number):
    '''
    returns the index of number in the prime_list, 
    or the index of the prime below it
    '''
    if number < 2 or number > latest_prime():
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
  
  
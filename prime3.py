#module for calculating and accessing primes, etc.

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
MAX_SET_SIZE = 1000

def prime_gen(upto):
  '''
  calculates the primes lower than upto (inclusively) 
  and stores them in prime_list. Returns None
  '''
  None

def latest_prime():
  '''
  returns largest prime calculated so far
  '''
  return prime_list[-1]
  
def nth_prime(n):
  '''
  returns the nth prime number (2 is the 1st prime, etc.)
  '''
  None
  
def is_prime(int):
  '''
  returns true if n is prime
  '''
  None
  
def get_ordinal(prime):
  '''
  returns the ordinal of a given prime (2 is the 1st prime, etc.)
  '''
  
def largest_under(number):
  '''
  returns the largest prime below number
  '''
  None
  
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
  None
  
  
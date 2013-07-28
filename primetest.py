#!C:\Python33\python.exe
import sys
import prime3
import timeit

i = 1000
stepsize = 1000000


while i < sys.maxsize:
  print('primes up to', i, 'in')
  comstring = 'primegen.primegen(' + str(i) +', ' + str(stepsize) +')'
  print(comstring)
  prime3.prime_gen(i)
  print(len(prime3.prime_list))
  #timeit.timeit(comstring, setup='import primegen')
  #timeit.timeit('primegen.primegen(100,1000000)', setup='import primegen')
  i=i*10


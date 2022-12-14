##Tells if number is prime or not
def isPrime(n):
  if n == 2 or n == 3: return True
  if n<2 or n%2 == 0: return False 
  
  for x in range(3,int(n**0.5)+1,2):
    if n%x == 0:
      return False
      
  return True
  



##Tests for perfect number, uses Euler Euclid Formula:
##Perfect number = (2**p)(2**p - 1)/2
##Where (2**p)-1 is prime

def isPerfect(p):
  ##Denote 2**p as t to make it look nicer
  t = (2**p)
  
  ##If t-1 is prime, must have perfect number
  if isPrime(t-1):
  
    ##Find Perfect number, n and print
    n = t*(t-1)/2
    print("Perfect number found: {} \n".format(n))
    
    
def main():
  p = 0
  while True:
    p += 1
    isPerfect(p)
   
   
##If name main to look fancy
if __name__ == "__main__":
  main()

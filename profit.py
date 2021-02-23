import math

#Return (n choose k)
def binom(n, k):
  return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

def main():
  res = [0,0,0,0,0,0,0,0,0,0,0]
  for n in range(11):
    sum1 = 0
    sum2 = 0
    lastn = 0
    for x in range(n):
      sum1 += ((150 * x) - (100 * n)) * binom(10,x) * math.pow(0.5, 10)
      lastn = x
    for x in range(lastn+1, 11):
      sum2 += (50 * n) * binom(10,x) * math.pow(0.5, 10)
    res[n] = sum1 + sum2
  
  return 0;


    

if __name__ == "__main__":
    main()
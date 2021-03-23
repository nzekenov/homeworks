import math

def main():
  vals = [0,0,0,0,0,0,0,0,0,0,0]
  for ma in range(11):
    for i in range(1,11):
      for j in range(2,11):
        for k in range(3,11):
          if (max(i,j,k) == ma):
            vals[ma]+=1
  for i in range(11):
    vals[i] = vals[i] / 720
  print(vals)
  return 0;

    

if __name__ == "__main__":
    main()

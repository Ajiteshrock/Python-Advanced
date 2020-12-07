def  countSetBits(n,k):
    ct=0
    res = [n[i: j] for i in range(len(n)) 
          for j in range(i + 1, len(n) + 1)]

    for i in range(len(res)):
        binary_num = res[i]
        count = 0
        i=0
        while (i<len(binary_num)): 
            if binary_num[i] == '1':  
               count+=1
            i+=1
        if count==k:
            ct+=1
    return ct
    
  

t = int(input())
while t>0:
    length=int(input())
    test_str = input()
    k = int(input())
    print(countSetBits(test_str,k)) 
    t-=1
  
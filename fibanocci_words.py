
# Enter your code here. Read input from STDIN. Print output to STDOUT



# Enter your code here. Read input from STDIN. Print output to STDOUT


def fib(container,la,lb,n):
    tl=la + 2*lb
    r=n%tl
    #r=mod(str(n),tl)
    #print("r is"+str(r))
    if r==1:
        print(container[0])
    else:
        sub=r-1
        start=n-sub
        l=len(container)
        dif=n-start
        index=dif%l
        print(container[index])


def mod(num, a): 
      
    # Initialize result 
    res = 0
  
    # One by one process all digits 
    # of 'num' 
    for i in range(0, len(num)): 
        res = (res * 10 + int(num[i])) % a; 
  
    return res 

q=int(input())
for i in range(q):
    line=(input()).split(" ")
    a=line[0]
    b=line[1]
    n=int(line[2])
    len_a=len(a)
    len_b=len(b)
    container=list(a)+list(b)+list(b)
    #print(container)
    fib(container,len_a,len_b,n)
    

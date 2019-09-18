
def fib(container,la,lb,n):
    tl=la + 2*lb
    r=n%tl
    #print("r is"+str(r))
    if r==1:
        print(str(container[0]))
    else:
        sub=r-1
        start=abs(n-sub)
        l=len(container)
        index=(abs(n-start))%l
        print(str(container[index]))




q=int(input())
for i in range(q):
    line=(input()).split(" ")
    a=line[0]
    b=line[1]
    n=int(line[2])
    len_a=len(a)
    len_b=len(b)
    container=list(a)+list(b)
    #print(container)
    fib(container,len_a,len_b,n)

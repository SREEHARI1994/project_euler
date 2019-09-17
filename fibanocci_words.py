# Enter your code here. Read input from STDIN. Print output to STDOUT


def fib(a,b,la,lb,n):
    tl=la + 2*lb
    r=n%tl
    #print("r is"+str(r))
    if r==1:
        print(a[0])
    else:
        sub=r-1
        start=n-sub
        while True:
            Done=False
            present_in_a=False
            for i in range(la):
                if start==n:
                    Done=True
                    present_in_a=True
                    break
                start=start+1
            if Done:
                break
            for i in range (lb):
                if start==n:
                    Done=True
                    break
                start=start+1
            if Done:
                break
            for i in range (lb):
                if start==n:
                    Done=True
                    break
                start=start+1
            if Done:
                break
        if present_in_a:
            #print("a pos"+str(i))
            print(a[i])
        else:
            #print("b pos" + str(i))
            print(b[i])
            
                








q=int(input())
for i in range(q):
    line=(input()).split(" ")
    a=line[0]
    b=line[1]
    n=int(line[2])
    len_a=len(a)
    len_b=len(b)
    fib(a,b,len_a,len_b,n)
    

   
    



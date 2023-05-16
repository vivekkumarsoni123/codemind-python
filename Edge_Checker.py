a,b=map(int,input().split())
if (a==1 and b==10) or (a==10 and b==1):
    print('Yes')
else:    
    for i in range(1,11):
        if (a==i and b==i+1) or (a==i+1 and b==i):
            print('Yes')
            break
    else:
        print('No')    
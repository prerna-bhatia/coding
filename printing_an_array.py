a=[10,20,30,40,50]
num=len(a)
def f(a,i):
   if i>=num:
      return
   else:
        print(a[i],end= " ")
        f(a,i+1)
       
print(f(a,0))
n=int(input('enter n :'))

def f(n):
   if n<1:
       return
   print(n,end= ' ' )
   f(n-1)
f(n)
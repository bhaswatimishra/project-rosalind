def fibbonaci() :
    n= int(input(f"Enter the number of months"))
    k= int(input(f"Enter the pair of rabbits produced by each reproducible pair"))
    a =1
    b=1
    if n == 1 or n == 2:
        print(f"The number of rabbits at the end of {n} months is : 1")
        return

    for i in range (3,n+1) :
        new = (a) + ((b)*k)
        b=a
        a=new
    print(f"The number of rabbits at the end of {n} months is : {a}")
fibbonaci()

'''
   #include<stdio.h>
   int main()
   {
   int a,b,c,d,e,i;
   printf("Enter the number of months");
   scanf("%d",&a);
   printf("Enter the pair of rabbits produced by each reproducible pair");
   scanf("%d", &b);
   c=1;
   d=1;
   for(i=3; i<= a; i++)
   {
     e = c + (d*b);
     d=c;
     c=e;
   }
   printf("The number of rabbits at the end of %d months is : %d",a,c);
   return 0;
   } 
'''

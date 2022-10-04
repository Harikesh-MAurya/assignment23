# 1. Use iter and next method to access all the elements of a given set using while loop
# 2. Create a generator to produce first n odd natural numbers
# 3. Create a generator to produce first n even natural numbers
# 4. Create a generator to produce squares of first N natural numbers
# 5. Create a generator to produce first n terms of Fibonacci series
# 6. Create a generator to produce first n prime numbers
# 7. Create an endless iterator using generator method to produce terms of Fibonacci
# series
# 8. Create an endless iterator using generator method to produce Prime numbers
# 9. Define a function which takes lengths of three sides of a triangle as arguments and
# display the perimeter or triangle. Define and apply a decorator which checks for the
# validity of the triangle on the basis of lengths of the side. This makes the perimeter to
# be displayed when the triangle can exist with the given lengths of the sides.
# 10. Define a function which calculates HCF of two numbers. Define and apply a
# decorator to check whether two given numbers are co-prime or not.


# 1) ...........................................
# a={1,2,3,4,5,6,7}
# s=iter(a)
# i=1
# while i<=len(a):
#     print(next(s),end=' ')
#     i+=1
    
    
# 2) ............................................
# def gen_odd(n):
#     x=1
#     while n!=0:
#         yield x
#         x+=2
#         n-=1
# l1=[]
# for e in gen_odd(int(input('enter n : '))):
#     print(e,end=' ')
    
    
# 3) ............................................
# def gen_odd(n):
#     x=2
#     while n!=0:
#         yield x
#         x+=2
#         n-=1
# l1=[]
# for e in gen_odd(int(input('enter n : '))):
#     print(e,end=' ')


# 4) ...........................................
# def square(n):    
#     while n>0:
#         yield pow(n,2)
#         n-=1
    
# l1=[i for i in square(int(input("Enter n : ")))]
# l1.reverse()
# print(l1)

# 5) .................................................
# def fib(n):
#     a,b=0,1
#     while n!=0:
#         yield a
#         a,b = b,a+b
#         n-=1
# for e in fib(int(input("enter n : "))):
#     print(e,end=' ')


# 6) ............................................
# from operator import ne


# def prime(n):
#     for i in range(1,n):
#         if i>0:
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 yield i
                
# t1=prime(20)
# prime(next(t1))


# 7) ........................................
# def fib_endless():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
        
# t1=fib_endless()

# while True:
#     ans=input("Enter [y/n] : ")
#     if ans=='y':
#         print(next(t1))
#     else:
#         break


# 9) ................................
# def trangle_existence(check):
#     def check(marks):
#         s=0
#         c=0
#         for i in marks:
#             s+=i
#             c+=1
#         print(s)  
#         s3=int(input("Enter third argument : "))
#         if c==2 and s>s3:
#             p=s+s3
#             print("Trangle will exist and its perimeter",p)
#         else:
#             check(marks)
            
#     return check

# @trangle_existence     
# def perimeter(marks):
#     s=0
#     for i in marks:
#         s+=i
#     print('the perimeter of the trangle is : ',s)

# marks=[20,20]
# perimeter(marks)


# 10) ........................................
# num1 = int(input("Enter first number: "))  
# num2 = int(input("Enter second number: "))

# i = 1
# while(i <= num1 and i <= num2):
#     if(num1 % i == 0 and num2 % i == 0):
#         gcd = i
#     i = i + 1

# print("The H.C.F. of", num1,"and", num2,"is", gcd, "".format(num1, num2, gcd))
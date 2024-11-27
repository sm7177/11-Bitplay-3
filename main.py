# a=int(input("Enter a number:"))
# b=int(input("Enter another number:"))

# a=a+b
# b=a-b
# a=a-b

# print("After swapping, the values are: a =",a, "and b =",b)








# def swap(a,b):
#     a=a^b
#     b=a^b
#     a=a^b
#     print("After swapping, the values are: a =",a, "and b =",b)
    
# swap(2,3)








# def swap(a,b):
#     a=(a&b)+(a|b)
#     b=a+(~b)+1
#     a=a+(~b)+1

#     print("After swapping, the values are: a =",a, "and b =",b)

# swap(2,3)










def divide(ourdividend,ourdivisor):
    sign=(-1 if ((ourdividend <0)^(ourdivisor <0))else 1)
    ourdividend=abs(ourdividend)
    ourdivisor=abs(ourdivisor)
    
    quo=0
    temp=0
    for i in range(31, -1, -1):
        if temp + (ourdivisor << i) <= ourdividend:
            temp += ourdivisor << i
            quo |= 1 << i
    if sign ==-1:
        quo=-quo
    return quo
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))

print("The answer is",divide(a,b))
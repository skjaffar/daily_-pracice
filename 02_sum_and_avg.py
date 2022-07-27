""" Sum and Average of 3 Numbers """
a,b,c=[float(x) for x in input("Enter 3 Numbers:").split(',')]
sum=a+b+c
avg=sum/3
print("The Sum is %.2f\nAverage is %.2f" %(sum,avg))

# s=10,20,30
# r=sum(s)
# print(r)
# av=r/3
# print(av)




# a,b=[float(x) for x in input("enter two numbers:").split(',')()]
# sum=a+b
# avg=sum/2
# print("the sum is %.2f\naverage is %.2f" %(sum,avg))

a,b,c=[float(x) for x in input("enter the three values:").split(' ,')]
sum=a+b+c
avg=sum/3
print("the sum is%.2f\naverage is%.2f" %(sum,avg))
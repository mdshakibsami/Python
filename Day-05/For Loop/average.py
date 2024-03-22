numbers = input('enter numbers:\n').split()
sum=0 
count=0
for num in numbers:
    count+=1
    sum+=int(num)
avg = sum/count
print(avg)
print(round(avg))
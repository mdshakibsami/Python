x= open("Others/File Handling/demo.txt")
data1 = x.read(5)
print(data1)
#if we want with no new line use end='' in previous print()
data2 = x.read(6)
print(data2,end='')
#if you want to read enter file
data3 = x.read(4)
print(data3)
data = x.read()
print(data)
#length of data
l =len(data)
print(f"{l} byte")
x.close()
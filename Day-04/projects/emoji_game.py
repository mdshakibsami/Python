row1 =["😊","😊","😊"]
row2 =["😊","😊","😊"]
row3 =["😊","😊","😊"]
squre = [row1,row2,row3]
position = input("Enter two digit number: ")
a = int(position[0])-1
b = int(position[1])-1
squre[a][b]="😍"
print(f"{row1}\n{row2}\n{row3}")

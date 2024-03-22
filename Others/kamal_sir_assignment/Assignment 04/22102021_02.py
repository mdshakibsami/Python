#function with parameter and return value:

def substring_count (str,sub_str):
    l=len(str)
    lsub=len(sub_str)
    start=count=0
    end=l
    while True:
        position=str.find(sub_str,start,end)
        if position!=-1:
            count+=1
            start=position+lsub
        else:
            break
        if start>=l:
            break;
    return count
str=input("Enter a String : ")
sub_str=input("Enter a sub String : ")

x=substring_count(str,sub_str)
print(x)
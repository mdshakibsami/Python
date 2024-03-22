'''
---------------code----------------
'''
str=input("Enter a String : ")
substr=input("Enter a sub String : ")
l=len(str)
lsub=len(substr)
start=count=0
end=l
while True:
    position=str.find(substr,start,end)
    if position!=-1:
        count+=1
        start=position+lsub
    else:
        break
    if start>=l:
        break;
print(count)

'''
----------------------------How it workes----------------
1>>> 
"str" and "substr" take input two line of string respectively

2>>> 
"l" and 'lsub' count the length of "str" and 'substr' 

3>>> 
put the value of these variables 'start' and 'count' are 0
and 'end' = l

4>>>
This 'while loop' will not stop untill the condition is false

5>>>
Inside the loop, it uses the find method of strings to search
for the substr in the s string, starting from the start position 
and ending at the end position. It stores the result in the position variable.

6>>>
If position is not equal to -1 (indicating that the substring was found), 
it increments the count by 1 and updates the start position to the position 
immediately after where the substring was found.

7>>>
If the start position becomes greater than or equal to the length of the main 
string s, the loop breaks, as there are no more substrings to find in the 
remaining portion of the string.

8>>> 
Finally return the value of "count"
'''
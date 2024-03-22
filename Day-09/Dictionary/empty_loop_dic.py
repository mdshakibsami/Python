#empty dictionary
empty ={}
empty["one"]=1
empty["two"]=2
empty["three"]=3
print(empty)
#loop through the dictionay
for key in empty:
    print(f"key={key}")
    print(f"value={empty[key]}")

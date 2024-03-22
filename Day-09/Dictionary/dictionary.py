dictionary ={
"Shakib":"He is a good boy",
"Samiya":"She is very good girl",
"Srabon":"Good Man",
}
print(f"1st={dictionary}")
#printing values using keys
print(dictionary["Samiya"])
#inputing new value in dictionary 
dictionary["Shafin"]="Very good Man"
print(f"2nd= {dictionary}")
#replacing value in dictionary
dictionary["Shakib"]="Sometimes becomes so bad"
sk=dictionary["Shakib"]
print(f"sakib={sk}")
#Empty the list
dictionary={}
print(f"Empty dic:{dictionary}")
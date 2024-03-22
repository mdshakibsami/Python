#list is Array(in C language) like data_structure
states_of_america = ["delaware","pennsylvania","new jersy","georgia","connecticut","maryland","new maxico"]
#printing a list
print(states_of_america)
#indexing start from 0 to n
state = states_of_america[0]
print(state)
#nagetive indexing is possible.It starts [-1] from back
state = states_of_america[-1]
print(state)
#replace value using index
state =states_of_america[0]="new York"
print(state)
#list length
print(len(states_of_america))
#list could be mixed data_type
list1 = ["abc", 34, True, 40, "male"]
print(list1)
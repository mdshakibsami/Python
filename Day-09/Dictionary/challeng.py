travel_log_list = [
    {
        "country":"France",
        "visited_cities":["Paris","Lille","Dijon"],
        "Total_cities":23,
        },
    {
        "country":"Germany",
        "visited_cities":["Berlin","Hamburg","Stuttgart"],
        "Total_cisties":10
        }
 ]

#the function
def add_new_country(country,visited_cities,total_cities):
    new_dic={
        "country":country,
        "visited_citiyes":visited_cities,
        "Total_cities":total_cities,

    }
    travel_log_list.append(new_dic)

#challenge>>Write a function that will work with the following line
#of code on line 21 to add the entry for Russia to the travel_log
add_new_country(country="Russia",visited_cities=["Moscow", "Saint Petersburg"],total_cities=2)

print(travel_log_list)
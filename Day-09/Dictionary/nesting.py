capital ={
    "France":"Paris",
    "Germany":"Berlin",

}
#nesting a list in a Dictionary
travel_log = {
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"]
}
#nesting Dictionary in a Dictionary
travel_log_dic = {
    "France":{
        "visited_cities":["Paris","Lille","Dijon"],
        "Total_cities":23,
        },
    "Germany":{
        "visited_cities":["Berlin","Hamburg","Stuttgart"],
        "Total_cisties":10
        }
}

#nesting Dictionary in List

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
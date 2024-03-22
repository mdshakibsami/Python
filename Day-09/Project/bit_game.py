
bid_dic={}
bidding_finished = False
while not bidding_finished:
    name = input("Enter canditate name: ")
    price = int(input("Enter your bit price: "))
    bid_dic[name]=price
    stop_signal = input("type 'yes' for new bit ,other wise 'no' ")
    if stop_signal=="no":
        bidding_finished=True

def winner(dictionary):
    max_bid =-1
    for person in dictionary:
        bid_price = dictionary[person]
        if bid_price>max_bid:
            bid_name = person
            max_bid = bid_price
    print(f"Winner is {bid_name} with a bid {max_bid}$.")

winner(bid_dic)
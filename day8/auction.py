from auction_art import logo
import os

print(logo)
bidders = {}
continue_bid = True


def add_bider():
    name = input("please give us your name. ")
    bid = int(input("how much do you want to bid? "))
    bidders[name] = bid


while continue_bid:
    add_bider()
    continue_bidding = input(
        'do you have another bidder? type "yes" to continue. ')
    if continue_bidding == "yes":
        os.system("clear")
    elif continue_bidding == "no":
        continue_bid = False
        highest_bidder = ""
        highest_bid = 0
        for bid in bidders:
            if bidders[bid] > highest_bid:
                highest_bid = bidders[bid]
                highest_bidder = bid
        print(f"the highest bidder is {highest_bidder} with {highest_bid}")

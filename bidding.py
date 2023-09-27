bids={}
bidding_over=False

def find_highest_bidder(bid_record):
    highest_bid=0
    winner=""
    for bidder in bid_record:
        bid_amnt=bid_record[bidder]
        if bid_amnt>highest_bid:
            highest_bid=bid_amnt
            winner=bidder
    print(f"The winner is {winner} with a bid amount of ${highest_bid}.")

    print('''
                               ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\   ''')

print("Welcome to the secret auction program.")

while not bidding_over:
    name=input("What is your name?: ")
    price=int(input("What's your bid price?: $"))
    bids[name]=price
    want_continue=input("Are there more bidder? Type 'yes' or 'No'.\n")
    if want_continue =="No".lower():
        bidding_over=True
find_highest_bidder(bids)
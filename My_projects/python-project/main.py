from replit import clear
bids = {}
bidding_finished = False

def find_hightest_bidder(bidding_record):
    hightest = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > hightest:
            hightest = bid_amount
            winner = bidder

    print(f"The winner is {winner} with the bid of {hightest}.")


while not bidding_finished:
    name = input("What is your nice name: ")
    price = int(input("What is your bid: $"))
    bids[name] = price
    should_continue = input("Are there any other bidder? type 'yes' or 'no': ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_hightest_bidder(bids)
    elif should_continue == "yes":
        clear()
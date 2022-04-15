import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

clearConsole = lambda: print('\n' * 150)



bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")



while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid? $"))
  bids[name] = price

  more_bids = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if more_bids == "no":
    bidding_finished = True
    highest_bidder(bids)
  elif more_bids == "yes":
    clearConsole()
  

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

#HINT: You can call clear() to clear the output in the console.
print(logo)
close = True
bids = {}
bid_value = []
while close:
   name = input('tell me ur name : ')
   your_bid = input('what is your bid :')
   bids[name] = your_bid
   next = input('is there anyother bidders "yes" or "no"')
   if next == 'no':
      close = False
   elif next == 'yes':
       clear()
for x in bids:
    bid_value.append(bids[x])
a = max(bid_value)
for x in bids:
    if a == bids[x]:
       print(f'the highest bidder is {x}')

   
    
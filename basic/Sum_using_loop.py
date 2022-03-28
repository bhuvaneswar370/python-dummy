#Averaging the prices after the loop ends

from asyncio.windows_events import NULL

total=0
prices = [2.50, 3.50, 4.50]
for price in prices:
      total=total+price
average = total/len(prices)
print("avg is", average)
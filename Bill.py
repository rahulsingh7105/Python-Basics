import datetime
now=datetime.datetime.now()
dtm=str(now)			#current date and time converted to string
item="Amul Butter 100gms"
price=45
qty=4
val=price*qty			#amount calculated
tax=val*0.05			#5%tax
net=val+tax				#net payable amount
print("-"*65)
print("\t\t\t\tInvoice")
print("-"*65)
print()
print("Date: {0:>55s}".format(dtm))
print("-"*65)
print("Item\t\t\t Unit price\tQuantity\t Value")
print("-"*65)
print("{0:<25s}".format(item),end="")
print("{0:>7.2f}".format(price),end="")
print("{0:>10d}".format(qty),end="")
print("{0:>14.2f}".format(val))
print()
print("Tax:{0:>57.2f}".format(tax))
print("-"*65)
print("Amount Payable:{0:>46.2f}".format(net))
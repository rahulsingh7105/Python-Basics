totaltrans, totalsales =0,0
n=1
while n<=3:
	trans=int(input("Transaction made on day"+str(n)+":"))
	items=int(input("Items sold on day"+str(n)+":"))
	totaltrans +=trans
	totalsales +=items
	n+=1
Avgsales=totalsales/totaltrans
print("Total sales made:",totalsales)
print("Total transaction made:",totaltrans)
print("Average sales per transaction:",Avgsales)
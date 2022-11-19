a = 20 
b = 10 
c = 15 
d = 5  
print ("a:%d b:%d c:%d d:%d" % (a,b,c,d )) 
e = (a + b) * c / d       #( 30 * 15 ) / 5 
print ("Value of (a + b) * c / d is ",  e)  
e = ((a + b) * c) / d     # (30 * 15 ) / 5 
print ("Value of ((a + b) * c) / d is ",  e)  
e = (a + b) * (c / d)    # (30) * (15/5) 
print ("Value of (a + b) * (c / d) is ",  e)  
e = a + (b * c) / d      #  20 + (150/5) 
print ("Value of a + (b * c) / d is ",  e) 
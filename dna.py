print("Welcome to the Indian BioInformatics.")
print("Designed or Created by Rahul Singh and Aman Krishna")
print("Under the Guidance of Ghoshal Sir.")
DNA=input("Enter Your DNA sequence below:\n")
DNA_upper=DNA.upper()
#print(DNA_upper)
DNA_upper_reversed=DNA_upper[::-1]
print("The reverse DNA strand is:\n"),#DNA_upper_reversed)
for i in DNA_upper_reversed:
	if(i=="A"): print("T",end= "")
	elif(i=="T"): print("A",end= "")
	elif(i=="C"): print("G",end= "")
	elif(i=="G"): print("C",end= "")
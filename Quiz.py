score = 0
score = int(score)

#Ask user for their name
name = input("What is your name: ")
print()
name = name.title()
print("""Hello {}, welcome to Iron Man Quiz Show! 
You will be presented with 5 questions.
Enter the appropriate number to answer the question
Good luck!""".format(name))
print()
#Question1
print("What is the Capital of India?\n1. Karnataka\n 2.Delhi")

a = "2"
response1 = input("Your answer is:")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response1 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")
print()
#Question2
print("""Which one of this is a flightless bird?
1. Parrot
2. Kiwi
3. Sparrow
4. Pigeon""")

answer2 = "2"
response2 = input("Your answer is:")

if (response2 != answer2):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response2 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")
print()
#Question3
print("""Who is our first President of India ?
1. Rajendra Prasad
2. Jawaharlal Nehru
3. Mahatma Gandhi 
4. Bhagat Singh""")

answer3 = "1"
response3 = input("Your answer is:")

if (response3 != answer3):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response3 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")
print()
#Question4
print("""When Mahatma Gandhi died?
1. 30 May 1948
2. 20 August 1947
3. 30 January 1948
4. 15 June 1949""")

answer4 = "3"
response4 = input("Your answer is:")

if (response4 != answer4):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response4 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")
print()
#Question5
print("""Who designed PUBG?
1. Raymonf F Boyce
2. Brendan Greene
3. Darren sugg
4. Carryminati""")

answer5 = "2"
response5 = input("Your answer is:")

if (response5 != answer5):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response5 + " is correct!")
    score = score + 1
print()
print("Your total score is " + str(score) + " out of 5")
print("Thank you for playing {}, goodbye!".format(name))
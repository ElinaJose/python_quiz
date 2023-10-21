print("Welcome to the quiz!")

playing = input("Enter 'yes' to proceed or anything else if you want to quit: ")

if playing.lower() != "yes":
    quit()

name = input("\bWhat is your name? ")
print("\b")
print("\bHello, " + name + ". I challenge you to answer all these 5 questions to test your general knowledge.")
print("Each one correct answer will account to a score of 1.")
print("The total mark will be calculated and shown after you finished answering all. Good luck!")
print("\b")

score = 0

answer = input("What does RAM stand for? Please write it in full and with the CORRECT spelling. Hint: 3 words.  ").lower()
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("\b")
answer = input("What is the national flower of Ukraine?  ").lower()
if answer == "sunflower":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("\b")
answer = input("What is the capital city of Australia? Hint: Not Sydney.  ").lower()
if answer == "canberra":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("\b")
answer = input("Who is the Minister of Tourism, Arts and Culture in Malaysia? Hint: First name is Tiong.  ").lower()
if answer == "tiong king sing":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("\b")
print("Congrats! You got " + str(score) + " questions correct!")
print("Your total mark is " + str((score/4) * 100) + "%!")
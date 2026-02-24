import random

name = "Krishna"
question = "Will I win the game?"
answer = ""

# Generating a random number
random_number = random.randint(1,11)
#print(random_number)

# Assigning answers based on random number

answers = {1: "Yes - definitely", 2: "It is decidedly so", 3: "Without a doubt", 4: "Reply hazy, try again", 5: "Ask again later", 6: "Better not tell you now", 7: "My sources say no", 8: "Outlook not so good", 9: "Cannot predict now", 10: "Very doubtful", 11: "Signs point to yes"}
answer = answers.get(random_number, "Error")

# ALTERNATE WAY FOR THE ABOVE CODE

"""
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Cannot predict now"
elif random_number == 10:
  answer = "Very doubtful"
elif random_number == 11:
  answer = "Signs point to yes"
else:
  answer = "Error"
"""

# Seeing the result
if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
  if name == "":
    print("Question:", question)
  else:
    print(name, "asks:", question)
    print("Magic 8-Ball's answer:", answer)

# END OF THE CODE!
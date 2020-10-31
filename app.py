print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 5

tracker = 0

counter +=1
tracker +=1

while tracker ==1:
  
  print("Q"+str(counter)+") "+ "What is 15 - 3?")
  print("   a) 5")
  print("   b) 18")
  print("   c) 45")
  print("   d) 12")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is not division."
    score -=1
  elif answer == "b":
    output = "Wrong. This is not addition."
    score -=1
  elif answer == "c":
    output = "Wrong. This is not multiplication!"
    score -=1
  elif answer == "d":
    output = "This is correct!"
    tracker +=1
    score +=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

  counter +=1

while tracker ==2:
  
  print("Q"+str(counter)+") "+ "What is 7 * 6?")
  print("   a) 1.15")
  print("   b) 1")
  print("   c) 42")
  print("   d) 13")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is not division."
    score -=1
  elif answer == "b":
    output = "Wrong. This is not subtraction."
    score -=1
  elif answer == "c":
    output = "This is correct!"
    tracker +=1
    score +=1
  elif answer == "d":
    output = "Wrong. This is not addition!"
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  

  
counter +=1

while tracker ==3:
  
  print("Q"+str(counter)+") "+ "The chemical formula O2 represents")
  print("   a) one oxygen molecule")
  print("   b) one oxygen atom")
  print("   c) two oxygen atoms")
  print("   d) two oxygen molecules")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker +=1
    score +=1
  elif answer == "b":
    output = "Wrong. The number two here means that there are two molecules/atoms."
    score -=1
  elif answer == "c":
    output = "Correct. There are two oxygen atoms here."
    tracker +=1
    score +=1
  elif answer == "d":
    output = "Wrong. Recap about the definitions of an atom and molecule."
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1

while tracker ==4:
  
  print("Q"+str(counter)+") "+ "What is the noun form of attract?")
  print("   a) attracted")
  print("   b) attraction")
  print("   c) had attracted")
  print("   d) attractive")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is the past tense of attract."
    score -=1
  elif answer == "b":
    output = "Yes, that's right! The noun form of attract is attraction."
    tracker +=1
    score +=1
  elif answer == "c":
    output = "Wrong.  This is the past participle of attract."
    score -=1
  elif answer == "d":
    output = "Wrong. This is the adjective of attract."
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  
  
counter +=1

while tracker ==5:
  
  print("Q"+str(counter)+") "+ "What is 10 / 2?")
  print("   a) 5")
  print("   b) 12")
  print("   c) 8")
  print("   d) 20")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "This is correct!"
    tracker +=1
    score +=1
  elif answer == "b":
    output = "Wrong. This is not addition."
    tracker +=1
    score +=1
  elif answer == "c":
    output = "Wrong. This is not subtraction"
    score -=1
    
  elif answer == "d":
    output = "Wrong. This is not multiplication"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  
print("End of quiz!")

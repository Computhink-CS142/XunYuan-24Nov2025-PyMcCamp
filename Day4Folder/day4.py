# Write all your codes for Day 4 here.
# COMMENT out the previous task before going on to the next task
# print("hello from day4")

########################################################################
# Task 1:
# a
# counter = 0
# while counter < 10:
#     print(counter)
#     counter = counter + 1
# # b
# counter = 5
# while counter < 33:
#     print(counter)
#     counter = counter + 1 
# # c
# counter = 50
# while counter > 0:
#     print(counter)
#     counter = counter - 1


########################################################################
# Task 2:

answer = "gummy bear"

person_answer = input("what do you call a bear with no teeth?")
lives = 5

while person_answer != answer:
    person_answer = input("what do you call a bear with no teeth?") 
    lives = lives - 1
    if lives < 0:
        print("u have died")
print("ans correct")
print(lives)
########################################################################
# Additional exercises:
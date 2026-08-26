#!/usr/bin/python3
# This quest is about creating two functions that ask user their age and also if they can vot edepending on their age.
def ask_for_age():
    age = int(input("Enter your age: "))
    return age

def can_they_vote(age):
    if age >= 16:
        print("You can vote!")
    else:
        print("You are young to vote!")

user_age = ask_for_age()
can_they_vote(user_age)

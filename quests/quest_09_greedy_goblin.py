#!/usr/bin/python3
total_gold = 27
number_of_friends = 4

each_friends_share = total_gold // number_of_friends
gold_leftover = total_gold % number_of_friends

print(f"Each friend gets {each_friends_share} gold pieces.")
print(f"The goblin keeps {gold_leftover} gold pieces as leftovers.")

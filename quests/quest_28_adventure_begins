#!/usr/bin/python3
# This quest was about creating a simple text-based adventure game using functions and user input


def cave_room():
  print("\nYou entered a dark cave, and fell into a pit. Game Over! 💀")


def forest_room():
  print("\nYou are in a dark forest. You survived!")
  choice = input("Do you want to explore the forest or enter the cave? ").lower()

  if choice == "cave":
    cave_room()
  elif choice == "forest":
    print("You safely walked deeper into the trees and won! 🎉")
  else:
    print("Invalid choice. Try again!")
    forest_room()


def start_adventure():
  print("Welcome to the Adventure Game!")
  choice = input("Do you want to go to the 'forest' or the 'cave'? ").lower()

  if choice == "forest":
    forest_room()
  elif choice == "cave":
    cave_room()
  else:
    print("Invalid choice. Try again!")
    start_adventure()


# Run the game
start_adventure()

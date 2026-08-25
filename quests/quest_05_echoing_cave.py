#!/usr/bin/python3
player_health = 100
print(f"Starting health: {player_health}.")

# when a monster attacks
player_health = player_health - 25
print(f"After the monster attacks: {player_health}")

# when the player finds a potion
player_health = player_health + 10
print(f"After drinking the potion: {player_health}")

print(f"Final health: {player_health}")

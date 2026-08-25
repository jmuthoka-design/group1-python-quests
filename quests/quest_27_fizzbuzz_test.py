#!/usr/bin/python3
# This quest was about how to implement the FizzBuzz test
# Loop through numbers from 1 to 100
for i in range(1, 101):
  # 1. Check for BOTH multiples of 3 and 5 first!
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  # 2. Check for multiples of 3
  elif i % 3 == 0:
    print("Fizz")
  # 3. Check for multiples of 5
  elif i % 5 == 0:
    print("Buzz")
  # 4. If none of the above are true, just print the number
  else:
    print(i)

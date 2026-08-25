#!/usr/bin/python3
dragon_scale_cost = 10
elf_tear_cost = 3
 
dragon_scales_needed = 3
elf_tears_needed = 5
 
dragon_scale_subtotal = dragon_scale_cost * dragon_scales_needed
elf_tear_subtotal = elf_tear_cost * elf_tears_needed
 
total_cost = dragon_scale_subtotal + elf_tear_subtotal
 
print(f"The potion requires {dragon_scales_needed} dragon scales and {elf_tears_needed} elf tears.")
print(f"Dragon scales cost: {dragon_scale_subtotal} gold")
print(f"Elf tears cost: {elf_tear_subtotal} gold")
print(f"Total cost sums up to: {total_cost} gold.")

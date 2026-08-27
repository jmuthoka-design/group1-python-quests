direction = str(input("Do you go left or right: "))
if direction == "left":
    action = input("Do you swim or wait: ")
    if action == "swim":
        print("You dive in the water and discover a hidden treasure")
    else:
        print("You wait on the shore but nothing happens but the moment passes")
else:
    print("You go right and find only rocks. Nothing there")

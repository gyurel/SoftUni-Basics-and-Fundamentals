width = int(input())
length = int(input())
height = int(input())
number_boxes = input()

volume = width * length * height
volume_boxes_total = 0


while number_boxes != "Done":
    volume_boxes_total += int(number_boxes)
    if volume_boxes_total < volume:
        number_boxes = input()
    else:
        free_space = volume_boxes_total - volume
        print(f"No more free space! You need {free_space} Cubic meters more.")
        break
else:
    free_space = volume - volume_boxes_total
    print(f"{free_space} Cubic meters left.")

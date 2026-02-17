# Find the height of Pyramid from the number of blocks

def calculate_height_of_pyramid(blocks: int) -> int:
    height = 0
    temp = 0
    while True:
        height += 1
        temp += height
        if temp > blocks:
            height -= 1
            break
    return height


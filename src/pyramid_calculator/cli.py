from pyramid_calculator.calculator import calculate_height_of_pyramid

def main():
    try:
        blocks=int(input("Please enter the number of blocks:"))
        if blocks < 0:
            raise ValueError("Blocks cannot be negative")  
        height=calculate_height_of_pyramid(blocks)
        print("The height of the pyramid is:", height)
    except ValueError:
        print("You entered a wrong value, please run the program again")
    

if __name__=="__main__":
    main()







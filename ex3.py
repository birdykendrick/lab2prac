def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()

def display_main_menu():
    numlist = []
    print("Enter some numbers with a space")
    numbers = input("Please enter the numbers here: ")
    xxx = numbers.split(" ")

    for p in xxx:
        numlist.append(float(p))

    print(numlist)

main()
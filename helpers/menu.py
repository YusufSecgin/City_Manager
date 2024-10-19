def show_menu():
    print("=" * 56)
    print(" City Population and Mapping System Made by Yusuf Secgin".center(56))
    print("=" * 56)
    print("1- Display Entered City Information")
    print("2- Display the N Most Crowded Cities")
    print("3- Display the N Least Populated Cities")
    print("4- Generate the Entered City Map")
    print("5- Display all cities")
    print("6- Print Cities according to their populations")
    print("0- Exit")
    print("=" * 56)
    choice = input("Please enter your choice: ")
    return int(choice)

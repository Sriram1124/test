hungry = input("Are you hungry? (yes/no): ").strip().lower()

if hungry == "yes":
    print("Eat a samosa!")
    print("pizza")
else:
    thirsty = input("Are you thirsty? (yes/no): ").strip().lower()  
    if thirsty == "yes":  
        print("Drink water")
        print("Drink soda")
        print("Drink thumbsup")
    else:
        print("Let it be.")

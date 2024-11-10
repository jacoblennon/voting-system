print("Welcome to the voting centre! Please enter your age to continue.")

age = int(input("My age is... "))

if age < 18:
    print("Unfortunately, you cannot vote yet.")
elif age >= 18:
    print("Welcome to the voting centre!")
    
    # Initial voting loop
    while True:
        print("Please select your candidate for 2025: Sir Meow, Lady Kitten Whiskers, or Councillor Fur.")
        vote = input("I would like to vote for... ")

        # Check each candidate choice
        if vote == "Sir Meow":
            confirmation = input("You have selected Sir Meow, is this correct? (Yes/No) ").strip().lower()
            if confirmation == "yes":
                print("Thank you for voting for Sir Meow!")
                break
            else:
                print("Let's try again.")

        elif vote == "Lady Kitten Whiskers":
            confirmation = input("You have selected Lady Kitten Whiskers, is this correct? (Yes/No) ").strip().lower()
            if confirmation == "yes":
                print("Thank you for voting for Lady Kitten Whiskers!")
                break
            else:
                print("Let's try again.")

        elif vote == "Councillor Fur":
            confirmation = input("You have selected Councillor Fur, is this correct? (Yes/No) ").strip().lower()
            if confirmation == "yes":
                print("Thank you for voting for Councillor Fur!")
                break
            else:
                print("Let's try again.")

        # Invalid candidate choice
        else:
            print("Invalid candidate. Please choose from Sir Meow, Lady Kitten Whiskers, or Councillor Fur.")

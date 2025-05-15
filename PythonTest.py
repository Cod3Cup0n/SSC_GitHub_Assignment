# Simple dialogue program mimicking Tony Hawk Pro Skater

print("Hello Tony Hawk!")
print("How are you feeling today?")
print("1. Ready to skate!")
print("2. Taking a break.")

choice = input("Enter 1 or 2: ")

if choice == "1":
    print("Awesome! Time to pull off some sick tricks.")
elif choice == "2":
    print("Rest up, legend. Even Tony Hawk needs downtime.")
else:
    print("That's not an option, but keep on skating the world!")

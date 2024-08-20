#Task 1: Code Correction You are provided with
#  a Python script that is supposed to help in event planning, but it has errors. 
# Identify and fix them.
attendees = int(input("Enter number of attendees: "))   
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
print("A PA system and microphone should provide sufficient audio needs" if attendees < 100 else "Speak with a staff member to use the integrated sound system for audio needs")
food = input("Would you like vegetarian food?") 
print("Veggie Delight Caterers provides great vegetarian meals" if food == "yes"  else "Gourmet Meal Caterers does great all around catering")
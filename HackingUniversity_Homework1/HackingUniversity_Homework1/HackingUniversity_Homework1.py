# This is my first homework problem in Hacking University
# This program will ask about someones Pet and return information back to them

def main():
      pet = int(input("How many pets do you have?"))
      if(pet == 0):
        print("Oh That is alright. Have a nice day")    
      else:
        print ("Tell me about one of them")
        pet_name = input("What is your pet's name?")
        pet_kind = input("What kind of animal is your pet?")
        pet_color = input("What color is your pet?")

        print() # Prints a blank line

        print("You have {0} Pets! {1} is the pet you chose to talk about. This pet is a {2}, right? {1}'s color is {3}. Did I get all of the information right?".format(pet, pet_name,pet_kind,pet_color))

main()



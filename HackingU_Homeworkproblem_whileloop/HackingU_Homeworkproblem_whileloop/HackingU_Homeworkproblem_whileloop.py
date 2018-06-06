
def main():
    print("Welcome to the Carling Adventure Game")
    print()
    print("Please what activity you would like to explore")
    print()
    print("Your choices are: sailing, rock-wall, safari, cliff-diving")
    print()
  
    ch1="a"
    while(ch1 !=""):
        ch1 = input("Please enter your choice or type blank line to stop: ")
        if(ch1==""):
            break
        elif(ch1 == "sailing" or ch1 =="rock-wall" or ch1 == "safari" or ch1 == "cliff-diving"):
            print("You have chosen wisely!")
        else:
            print("Please choose again")
   
   
    print("{} would be a nice place to start".format(ch1))

main()







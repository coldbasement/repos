
def main():
    keep_going = "a" #initialize varables before they are used

    number_grades = 0

    grade_list =[]

    total =0

    print("Grade Average Calculator")

    print()

    while(keep_going != "No" and keep_going !="no"):

        grade = int(input("Enter a test grade: "))

        number_grades +=1

        grade_list.append(grade)

        keep_going = input("Add more grades?")

        print()
    for x in range(0,number_grades):
        total+=grade_list[x] #add up all grades in list

    print("Average of {} tests is {}".format(number_grades,total/number_grades))
    print()
    print(grade_list)
main()

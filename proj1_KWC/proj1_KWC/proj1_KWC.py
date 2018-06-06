# proj1_KWC.py
# Converts Total Price of Meal into Three tip total possibilities:
#  Excellent service = 20% of total ticket
#  Average service = 15% of total ticket
#  Poor service = 10% of total Ticket
# Input = Total Meal Ticket
# Process = Computes tip amount for all three possibilities and Totals for each
# Output = Users Sees all possibilities in USD and Total cost of Meal (2 decimal points)

def main():
     meal_No_Tip = float(input("Enter the cost of the meal: $ "))
     cost_of_Meal = '${:,.2f}'.format(meal_No_Tip)
     eTip = float(meal_No_Tip * .20)
     excellent_Tip = '${:,.2f}'.format(eTip)
     e_Total = meal_No_Tip + eTip
     excellent_Total = '${:,.2f}'.format(e_Total)
     aTip = float(meal_No_Tip *.15)

     average_Tip = '${:,.2f}'.format(aTip)
     a_Total = meal_No_Tip + aTip
     average_Total = '${:,.2f}'.format(a_Total)
     pTip = float(meal_No_Tip *.10)
     poor_Tip = '${:,.2f}'.format(pTip)
     P_total =  meal_No_Tip + pTip
     poor_Total = '${:,.2f}'.format(P_total)
     print("Cost of Meal:",cost_of_Meal)
     print("Excellent Service tip:", excellent_Tip, "total:" ,excellent_Total)
     print("Average Service tip:", average_Tip, "total:",average_Total)
     print("Poor Service tip:", poor_Tip, "total:", poor_Total)
main()

#input("Press Enter To Exit...")

# Oh I learned a ton From this Project. I stuggled with the currency Format, and
# trying to figure out the data types I was trying to add together
# I think this is way more simpliler in JavaScript which I took last Semester. I struggled
# with this assignement, but I had tons of fun with it. I like Python!


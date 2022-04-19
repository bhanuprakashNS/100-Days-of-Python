# ..........Tip Calculator ..............#
# Created and Modified by N.S.Bhanuprakash in Jan 2022.

#If the bill was $150.00, splits between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Formatting the result to 2 decimal places = 33.60

total_bill = input("what was the total bill? $")
Tip = input("How much % of bill would u like to give as a tip? ")
No_of_people = input("How many people to split the bill? ")
Total_bill_with_tip = float(total_bill)*(1+float(Tip)/100)
Each_person_share = Total_bill_with_tip/float(No_of_people)
# Each_person_share = round(Each_person_share,3)
Each_person_share = "{:.2f}".format(Each_person_share) #Round to two digits which shows zero too
print(f"Each person should pay: ${Each_person_share}")
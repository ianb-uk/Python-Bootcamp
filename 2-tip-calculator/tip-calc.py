print("\n\nWelcome to the tip calculator.")
totalBill = input("What was the total bill? £")
tipPercent = input("What % tip would you like to give? 10, 12, or 15 ")
noPeople = input("How many people to split the bill? ")

# print(type(totalBill))
# print(type(tipPercent))
# print(type(noPeople))
# all start as string 

#add a 1. to % to make for quicker maths formula 
tipPercent2 = "1."+tipPercent
# print(tipPercent2)

#convert to int/float
flt_totalBill = float(totalBill)
flt_tipPercent = float(tipPercent2)
int_noPeople = int(noPeople)

#check conversion
# print(type(flt_totalBill))
# print(type(flt_tipPercent))
# print(type(int_noPeople))

totalPerPerson = (flt_totalBill / int_noPeople) * flt_tipPercent
rndTotalPerPerson = round(totalPerPerson,2)
rndTotalPerPerson = "{:.2f}".format(totalPerPerson)
# print(type(rndTotalPerPerson))
strPerPerson = str(rndTotalPerPerson)
# print(type(strPerPerson))
strPerPersonBill = "£"+strPerPerson
print("Each person should pay: ",strPerPersonBill,"\n\n")



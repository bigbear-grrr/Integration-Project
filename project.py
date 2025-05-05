#Lillianmay Lancour
#A weekly budget planner
welcome="WELCOME"
x=0
for i in (welcome):
    x=x+1
    print(welcome[0:x])#range
first_name=input("What is your first name? :")
last_name=input("What is your last name? :")
first=str(first_name)
last=str(last_name)
users_name=(first+' '+last)#string operators (+):combines the first and last name
print ("Hello"+" "+users_name+"! Welcome to Vault, a budget planner designed to make budgetting easy.")
print("Vault can help you calculate...","your income","your expenses","your estimated savings","and help you budget your spending cash",sep="\n")
print("Budgeting can be stressful even with assistance so take a moment to grab a snack or take some deep breaths")
seconds=input("How long do you need to get ready? Please type a number :")#snack time
seconds=int(seconds)
def countdown (seconds):#countdown - parameter passing
    while seconds>0:
        print (seconds)
        seconds=seconds-1
countdown(seconds)
print("Alright lets get started. First lest figure out your weekly pay...")#calculating paycheck
hours_worked=float(input("How many hours did you work this week? :"))
pay_per_hour=float(input("What is your hourly wage? $"))
tips=float(input("How much did you make in tips this week $"))
subtotal=float(hours_worked*pay_per_hour) #numeric operator (*):both have numeric values so multiply hours worked by pay per hour to get the subtotal
tax=float(subtotal*0.055) #florida tax is 5.5 percent so to find the tax amount multiply the subtotal by 0.055
total_wo_tax=float(subtotal-tax) #numeric operator (-):total paycheck minus the tax
total_w_tip=float(total_wo_tax+tips) #numeric operator (+):total plus the weekly tips
print("Your pay for the week is $",format(total_w_tip,'.2f'),end="\n""\n") #total money in for the week
#bills
print("Now lets figure out how much of that paycheck needs to go towards bills...")
ans=not False
while ans:
    ans=input("Do you have to pay for housing? :")#housing?
    if ans=="yes":
        total_rent=float(input("What is the total cost of your living situation? $"))
        roomates=int(input("How many people are contributing towards the rent, including yourself? :"))
        housing_bill=(total_rent)/(roomates)
        print("Your housing bill comes up to $",format(housing_bill,'.2f'),end="\n""\n")
        ans=False
    elif ans=="no":
        print("Alright we can skip that section then.")
        housing_bill=0
        ans=None
    else:
        print("Please try again and type yes or no.")
#gas
print("Now lets calculate your gas bill...")#gas?
ans=True
while ans:
    ans=input("Do you have to pay for gas? :")
    if ans=="yes":
        weekly_milage=float(input("What is your weekly milage? :"))
        average_miles=float(input("How many miles do you get to the gallon? :"))
        avg_miles=(average_miles//1) #numeric operator (//):rounds down to allow flexability (better to have too much rather than not enough)
        gas_price=float(input("What is the gas price per gallon? $"))
        gas_bill=float(weekly_milage/avg_miles)*(gas_price)#numeric operator (/): miles divided by miles per gallon calculates the number of gallons needed
        print("Your gas bill comes up to $",format(gas_bill,'.2f'),end="\n""\n")
        ans=None
    elif ans=="no":
        print("Alright we can skip that section then.")
        gas_bill=0
        ans=None
    else:
        print("Please try again and type yes or no.")
#insurtance
print("Its time to go over your extra expences...")
print("For the following please type the total cost of each bill. If one does not apply to you please type 0.",end="\n""\n")
car_insurance_bill=float(input("Car insurance $"))
phone_bill=float(input("Phone bill $"))
gym_membership=float(input("Gym membership $"))
#other expenses
other=0
ans_2=True
while ans_2:
    ans_2=input("Do you have any other bills or subscriptions you would like to add? :")
    if ans_2=="yes":
        #num of loops=input(int("How many bills or subscriptions would you like to add")
        name_of_xtra_bill=input(str("What is this bill for? :"))
        other_cost=float(input("What is the cost? $"))
        print(name_of_xtra_bill,"$",format(other_cost,'.2f'))
        other=other+other_cost
    elif ans_2=="no":
        print("Alright great job limiting your extra expences.")
        ans_2=None
    else:
        print("Please try again and type yes or no.")
other_bills=(car_insurance_bill+phone_bill+gym_membership+other)
print("Your other bills and subscriptions come up to $",format(other_bills,'.2f'),end="\n""\n")
#leftover
spending_cash=(total_w_tip)-(housing_bill)-(gas_bill)-(other_bills)
print("Your leftover spending cash is about $",format(spending_cash,'.2f'))
if (spending_cash <= 0):
    print("Congrats you're broke :(")
else:
    print ("Congrats you're not broke :)")
#savings
print("Setting money aside in a savings account is",("very "*2),"important.")
ans_3=True
while ans_3:
    ans_3=input("Would you like to set money aside for retirement? :")
    if ans_3=="yes":
        print("How much would you like to place in your retirement account?.",end="\n""\n")
        retirement=float(input("Retirement $"))
        intrest_rate=float(input("Retirement intrest rate :"))
        years=float(input("How many years will your retirement funds be held for? :"))
        r_funds=retirement*(1+intrest_rate)**(years)#**:used to calc intrest #f=p(1+i/n)ny
        print("With the information provided your retirement funds will be at",format(r_funds,'.2f'),"after",(years),"years of intrest")
        ans_3=None
    elif ans_3=="no":
        print("That's fine if you're not quite there. You're moving in the right dirrection so keep it up.")
        retirement=0
        r_funds=0
        ans_3=None
    else:
        print("Please try again and type yes or no.")
ans_4=True
while ans_4:
    ans_4=input("Would you like to set money aside in other saving accounts? :")
    if ans_4=="yes":
        emergency_spending=float(input("Emergency spending $"))
        savings=float(input("Regular savings $"))
        ans_4=None
    elif ans_4=="no":
        print("Setting money aside for savings is important but dont get bent out of shape if you miss a week or two.")
        emergency_spending=0
        savings=0
        ans_4=None
    else:
        print("Please try again and type yes or no.")
money_left_after_savings = spending_cash - retirement - emergency_spending - savings
total_savings= emergency_spending + savings
if r_funds>0 and total_savings>0:
    print("Great job investing in yourself!")
elif r_funds>0 or total_savings>0:
    print("As John C. Maxwell said 'a budget is telling your money where to go instead of wondering where it went.' So keep up the good work.")
else:
    print ("Well done.")
if money_left_after_savings%1!=0:
    print("We'll round down your spending cash and put the extra change in savings as well.")
    money_left_after_savings=money_left_after_savings//1
else:
    None
print("Your left over money comes up to : $",format(money_left_after_savings,'.2f'))
print ("We want to make this experience enjoyable for you so please rate your experience on a scale of 1-10 on how enjoyable it was")

print("bye "*2)
#string operators (*):bye*2 outputs byebye
#numeric operators: %,**,/,//,+,-,*  (use and include explanation)
#string operators:*,+  (use and include explanation)
#50 lines of code

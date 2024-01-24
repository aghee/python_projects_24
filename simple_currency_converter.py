#1usd=160.77kes
#Pending---Capture user input to cater for any currency amounts
#try except for catching errors
#How to validate input from user???-should a negative number be converted?-edge cases??
#user enters amount to convert, if Y/y print--HERE IS YOUR....then function executes
#if N---enter a different amount?(y/n) if Y/y--Enter amount you wish to convert please
#if N/n/any other input apart from Y/y--exit program
#Useful resource:https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/
print('-------------------------Simple Currency Converter-------------------')

while True:
    try:
        num=float(input('Enter amount to convert here: '))
        if num<=0:
            print('UNABLE TO CONVERT A ZERO OR NEGATIVE AMOUNT!!!ENTER AGAIN!!!')
            continue
        print('Amount to convert is: ',num)
        
    except ValueError:
        print('Please enter a NUMERICAL value')
        continue
    num1=input(f'Do you wish to proceed with {num} entered?Y OR N :')
    if num1=='y'or num1=='Y':
        break
        #print('Your amount is:',num)
    elif num1 !='y' or num1!='Y':
        p=input('Do you wish to enter a different amount? Y OR N :')
        if p=='y' or p=='Y':
            continue
        else:
            print('Exiting the currency calculator...GOODBYE!!!')
            exit()

def calc_converter(**curr):
    converted_curr=list()
#iteration variables iterating over list of tuples of key-value pairs obtained from curr    
    for currency,rate in curr.items():
        converted=num*rate
        converted_curr.append((currency,converted))
    #print(converted_curr)
    for currency,amount in converted_curr:
        print(num,'from',currency,'to Ksh is:',round(amount,2))
curr={
    'USD':163.00,
    'UGX':0.043,
    'TSH':0.065,
    'SOUTH_KOREAN_WON':0.12,
    'POUND':195,
    'SWISS FRANC':187.48,
    'RWANDAN FRANC':0.13,
    'CAD':121.13
}
calc_converter(**curr)

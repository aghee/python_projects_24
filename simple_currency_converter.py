import sys
#1usd=160.77kes
#Pending---Capture user input to cater for any currency amounts
#try except for catching errors
print('-------------------------Simple Currency Converter-------------------')
#How to validate input from user???-should a negative number be converted?-edge cases??
#user enters amount to convert, if Y/y print--HERE IS YOUR....then function executes
#if N---enter a different amount?(y/n) if Y/y--Enter amount you wish to convert please
#if N/n/any other input apart from Y/y--exit program
#Useful resource:https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/
try:
    k=float(input('Enter amount you wish to convert please:'))
    print(f'Do you wish to convert{k} to KSH? Y OR N')
    m=input('Y or N')
    if m=='Y':
        print('HERE IS YOUR CONVERTED CURRENCY.THANK YOU.')
    else:
        sys.exit()
except:
    print('Please check the values you have entered!!!')
def calc_converter(**curr):
    converted_curr=list()
#iteration variables iterating over list of tuples of key-value pairs obtained from curr    
    for currency,rate in curr.items():
        converted=k*rate
        converted_curr.append((currency,converted))
    #print(converted_curr)
    for currency,amount in converted_curr:
        print(k,'from',currency,'to Ksh is:',round(amount,2))
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

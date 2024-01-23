#1usd=160.77kes
#Pending---Capture user input to cater for any currency amounts
#try except for catching errors
print('-------------------------Simple Currency Converter-------------------')
def calc_converter(usd,ugx,tsh,pound,korean_yang):
    converted_curr=list()
    for i in curr:
        converted=15*curr[i]
        converted_curr.append(converted)
    #print(converted_curr)
    for j in converted_curr:
        print('The amount you have converted from',i,'to Ksh is:',j)
curr={
    'usd':160.77,
    'ugx':30000,
    'tsh':45000,
    'korean_yang':185,
    'pound':195
}
calc_converter(**curr)
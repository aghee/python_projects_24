import random

name1=input('Kindly enter your name:')
print(f'Your name is:{name1}')
question=name1+' '+'asks: Will i win the lottery?'
answer=''
random_number=random.randint(1,20)
#print(random_number)

if random_number==1:
    answer+='Yes-definitely'
elif random_number==2:
    answer+='It is decidedly so'
elif random_number==3:
    answer+='Reply hazy, try again'
elif random_number==5:
    answer+='Ask again later'
elif random_number==6:
    answer+='Better not tell you now'
elif random_number==7:
    answer+='My sources say no'
elif random_number==8:
    answer+='Outlook not so good'
elif random_number==9:
    answer+='Very doubtful'
elif random_number==10:
    answer+='You are out of luck today!'
elif random_number==12:
    answer+='TRY AGAIN, YOU MAY WIN ONE DAY!'
elif random_number==14:
    answer+='Chances are low, just keep trying!!!'
else:

    answer+='Error'
print(question)
print('Magic 8-Ball\'s answer: '+answer)
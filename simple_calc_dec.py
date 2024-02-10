#approach_one
'''
def decorator_func(display_func):
    \'''Decorator function.\'''
    def wrapper(*args):
        add_num=0
        for i in args:
            add_num+=i
        return display_func(add_num)
    return wrapper

@decorator_func
def display(sum1):
    \'''Target function.\'''
    print('The sum is:',sum1)

#display=decorator_func(display)
display(8,9,10,11,12,13,19,21,88,99,101,858,89,96)
print(decorator_func.__doc__)
print(display.__doc__)#output is None why yet it has docstring?
'''
#approach_two

def decorator_func(display_func):
    '''Decorator function.'''
    def wrapper(*args,**kwargs):
        display_func(*args,**kwargs)
        add=sum(args)
        print('Sum is :',add)
        sub=args[0]-sum(args[1:])
        print('The subtraction result is:',sub)
        multiply=1
        for i in args:
            multiply*=i
        print('The multiplication is:',multiply)
        div=args[0]
        for i in args:
            div /=i
        print('The division is:',div)
        print('-----------NUMBER DIVISIBILITY---------------')
        while True:
            try:
                check_modulo=int(input('Please enter number here:'))
                if type(check_modulo)==int:
                    break
            except ValueError:
                print('THAT IS NOT A NUMBER.TRY AGAIN!!!')
                #continue
        while True:
                print('----------------Check divisibility of number entered--------------')
                options=\
                '''
        A.Divisible by 2
        B.Divisible by 3
        C.Divisible by 4
        D.Divisible by 5
        E.Divisible by 6
        F.Divisible by 7
        '''
                print(options)
                opt_selected=input('Which option have you selected?')
                if opt_selected=='A' or opt_selected=='a':
                    if check_modulo%2==0:
                        print('Number divisible by 2')
                    else:
                        print('Not divisible by 2, Quotient and remainder is:',divmod(check_modulo,2))
                if opt_selected=='B' or opt_selected=='b':
                    if check_modulo%3==0:
                        print('Number divisible by 3')
                    else:
                        print('Not divisible by 3, Quotient and remainder is:',divmod(check_modulo,3))
                if opt_selected=='C' or opt_selected=='c':
                    if check_modulo%4==0:
                        print('Number divisible by 4')
                    else:
                        print('Not divisible by 4, Quotient and remainder is:',divmod(check_modulo,4))
                if opt_selected =='D' or opt_selected=='d':
                    if check_modulo%5==0:
                        print('Number divisible by 5')
                    else:
                        print('Not divisible by 5, Quotient and remainder is:',divmod(check_modulo,5))
                if opt_selected =='E' or opt_selected=='e':
                    if check_modulo%6==0:
                        print('Number divisible by 6')
                    else:
                        print('Not divisible by 6, Quotient and remainder is:',divmod(check_modulo,6))
                if opt_selected =='F' or opt_selected=='f':
                    if check_modulo%7==0:
                        print('Number divisible by 7')
                    else:
                        print('Not divisible by 7, Quotient and remainder is:',divmod(check_modulo,7))
                if opt_selected not in ('A','B','C','D','E','F'):
                    proceed=input('Invalid Option. Would you like to proceed? Enter Y or N: ')
                    if proceed=='Y' or proceed=='y':
                        print('Kindly select an option from the list shown')
                        #While True runs indefinitely as the condition(code below it)
                        # will always be true, it needs a break statement to stop
                        # continue
                    else:
                        print('END OF OPTIONS.GOODBYE!!!')
                        break
        #return display_func(*args,**kwargs)
    return wrapper
@decorator_func
def display(*args,**kwargs):
    '''Target function.'''
    print('Values passed are: {}'.format(args) )

display(400,5)
# display=decorator_func(display)
# print(display.__name__)



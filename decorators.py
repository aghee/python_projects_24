def decorator_func(display_func):
    '''Decorator function.'''
    def add(*args,**kwargs):
        add_num=0
        for i in args:
            add_num+=i
        display_func(*args,add_num)
    # def sub(*args):
    #     sub_num=0
    #     for i in sub:
    #         sub_num-=i
    #     display_func(*args,sub_num)

    return add
def display(*args,**kwargs):
    '''Target function.'''
    print('The sum of {} is {}'.format(args,kwargs))

display=decorator_func(display)
display(8,9,8,7,8)

#import math
#print(dir(math))
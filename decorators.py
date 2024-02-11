#decorators
def decorator_function(original_func):
    def wrapper(*args,**kwargs):
        print(f'Wrapper executed this before {original_func.__name__}')
        return original_func(*args,**kwargs)
    return wrapper

'''
#decorator class
class decorator_class:
    def __init__(self,original_func):
        self.original_func=original_func #tie function with the instance of this class

    def __call__(self,*args,**kwargs):#behaves like the wrapper function
         print(f'Call method executed this before {self.original_func.__name__}')
         return self.original_func(*args,**kwargs)
'''
@decorator_function
def display_intro():
    print('This is the display_intro function!')
display_intro()

@decorator_function
def display_info(*args):
    print('This function has the following arguments {}'.format(args))

display_info('agy',888)
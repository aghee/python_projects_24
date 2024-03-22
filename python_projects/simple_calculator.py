'''
#target=9
class Trial1():
    def __init__(self,nums):
        self.nums=nums   
    def func1(nums):
        t=nums[0]+nums[1]
        return t
obj=Trial1()
obj.func1([2,7,11,15])
'''
'''
def whats_on_the_telly(penguin=None):
    if penguin is None:
        penguin = []
    penguin.append("property of the zoo")#why does this execute?
    return penguin
print(whats_on_the_telly())
'''
#import trialcode

activity=[]
def kyc():
    name=input('What is your name?')
    print('Welcome {} to your TO-DO List'.format(name).upper())
#create activity
def createActivity():
    act=input('Kindly enter activity here: ')
    activity.append(act)
    print(f'You have added {activity} to your list')

#view activity
def viewActivity():
    if activity ==[]:
        print('No activities available at the moment')
    else:
        print('Existing Activities')
        for index,item in enumerate(activity,start=0):
            print(index,'-->',item)
#delete activity
def deleteActivity():
    viewActivity()
    try:
        deleteact=int(input('Please select activity to delete: '))
        if deleteact<len(activity) and deleteact >=0:
            #remove an item from a specified position on a list/dictionary and return it
            activity.pop(deleteact)
            print(f'{deleteact} has been deleted from your list')
        else:
            print('Task missing from list. Please confirm!')
    except ValueError:
        print('Check your input!')

#__name__ special variable containing name of current module
if __name__=='__main__':
    kyc()
    while True:
        print('---****------****-------****--------****--------')
        print('Kindly select an option from the list below')
        print('1.Create a new activity')
        print('2.View activity')
        print('3.Delete activity')
        print('4.Exit')
        select=input('Enter your choice here: ')
        if select=='1':
            createActivity()
        elif select=='2':
            viewActivity()
        elif select=='3':
            deleteActivity()
        elif select=='4':
            break
        else:
            print('Invalid Input.Enter again!')
    print('ADIOS AND HAVE A GREAT DAY')
          

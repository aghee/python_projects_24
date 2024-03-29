import csv

with open('Global YouTube Statistics.csv','r') as file:
    # read=csv.reader(file)
    ready=csv.DictReader(file)
    # next(ready)
    # for row in ready:
    #     print(row['category'])
    '''
    Entertainment,Comedy,Music,Education,Gaming=0,0,0,0,0
    for row in ready:
        fav=row['category']
        if fav=='Entertainment':
             Entertainment+=1
        elif fav=='Comedy':
            Comedy+=1
        elif fav=='Music':
            Music+=1
        elif fav=='Education':
            Education+=1
        elif fav=='Gaming':
            Gaming+=1
print('Entertainment:',Entertainment)
print('Comedy:',Comedy)
print('Music:',Music)
print('Education:',Education)
print('Gaming:',Gaming)
'''  
    counts={}


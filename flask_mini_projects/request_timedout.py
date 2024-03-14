import requests
from requests.exceptions import Timeout

url='https://www.linkedin.com/'
# url='https://www.remotasks.com/en'
try:
    response=requests.get(url,timeout=15)#GET request to url with specified timeout
    response.raise_for_status()#throw exception if HTTP status code is not successful
    # May replace line 8
    '''
    if response.status_code != 200:
        print('failed',response.status_code)
    else:
        print('success!OK')
        '''

#catches timeout exception if request takes longer than specified time
except Timeout as to:
    print('Request timedout!',to)

#catches any other requests exceptions
except requests.exceptions.RequestException as re:
    print('Error occured!',re)

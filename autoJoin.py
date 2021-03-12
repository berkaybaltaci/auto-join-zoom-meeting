'''  
This was only tested on a 1080p windows machine. It will not work for different resolutions since a part of this script uses coordinates to click. 
On small screens or laptops make sure to set scaling to 100%.
If the script doesn't seem to work properly, launching cmd as administrator and running the script in the console might help.
'''

import random
import time
import schedule
import myUtil


def randomizeJoinTime(baseTime):
    return baseTime[:-1] + str(random.randint(4, 9))


def scheduleToJoin(joinTime, day, subjectFunc):
    joinTime = randomizeJoinTime(joinTime)

    try:
        if day.lower() == 'monday':
            schedule.every().monday.at(joinTime).do(subjectFunc)
        elif day.lower() == 'tuesday':
            schedule.every().tuesday.at(joinTime).do(subjectFunc)
        elif day.lower() == 'wednesday':
            schedule.every().wednesday.at(joinTime).do(subjectFunc)
        elif day.lower() == 'thursday':
            schedule.every().thursday.at(joinTime).do(subjectFunc)
        elif day.lower() == 'friday':
            schedule.every().friday.at(joinTime).do(subjectFunc)
        elif day.lower() == 'saturday':
            schedule.every().saturday.at(joinTime).do(subjectFunc)
        elif day.lower() == 'sunday':
            schedule.every().sunday.at(joinTime).do(subjectFunc)
    except:
        print("Couldn't schedule to join. Potential typo in 'joinTime' or 'day' variable.")


#  In my case, only 2 parameters vary while joining classes, which are subject name and 'canli ders' button.
#  So it was possible to simply create a function that returns a new function which auto joins classes.
lojik_func = myUtil.generateSubjectFunc('//*[@id="app-container"]/div[4]/div[2]/div/ul/li[2]/a/span[2]',
                                        '//*[@id="menu-223c1698-4649-492f-8a61-8f6eb80f8535"]/ul/li[2]/a/span')

turkce1_func = myUtil.generateSubjectFunc('//*[@id="app-container"]/div[4]/div[2]/div/ul/li[9]/a/span[2]',
                                          '//*[@id="menu-30d3c3c4-d0a0-4e16-9d72-fb49f47eaff1"]/ul/li[2]/a/span')

mikrodalga1_func = myUtil.generateSubjectFunc('//*[@id="app-container"]/div[4]/div[2]/div/ul/li[4]/a/span[2]',
                                              '//*[@id="menu-d31dad9d-4299-4782-89f0-0d5ca46dbbb9"]/ul/li[2]/a/span')

networking_func = myUtil.generateSubjectFunc('//*[@id="app-container"]/div[4]/div[2]/div/ul/li[7]/a/span[2]',
                                             '//*[@id="menu-82e5d5ca-9d0e-422b-a110-a7fb77afc051"]/ul/li[2]/a/span')

scheduleToJoin('09:00', 'monday', lojik_func)
scheduleToJoin('11:00', 'wednesday', turkce1_func)
scheduleToJoin('15:00', 'thursday', networking_func)
scheduleToJoin('14:00', 'friday', mikrodalga1_func)


print('*** OLCEGI %100 YAPMAYI UNUTMA ***')
print('*** OLCEGI %100 YAPMAYI UNUTMA ***')
print('*** YONETICI OLARAK CALISTIRMAYI UNUTMA ***')
print('*** YONETICI OLARAK CALISTIRMAYI UNUTMA ***')


while True:
    schedule.run_pending()
    time.sleep(5)

import notify2
import schedule as scheduler
import time

class scheduleDic(dict):
    def __init__(self):
        self = dict()

    def add(self, name, time, description):
        self[name] = [time, description]

    def remove(self, key):
        self.pop(key)

def createSchedule():
    schedule = scheduleDic()

    moreEvents = True
    while moreEvents:
        event = input('What is the name of your first event: ')
        time = input('What time does this event take place: ')
        description = input('Give me a description of this event: ')
        schedule.add(event, time, description)
        moreEvents = input('anymore events? (y/n) ') == 'y'
    return schedule

def sendNotify(eventName, description, schedule):

    if eventName in schedule:
        notify2.init("That does this do")
        note = notify2.Notification(f"Time to {eventName}", description)
        note.set_timeout(900)
        note.show()
    else:
        return scheduler.CancelJob

def setUpSchedule(schedule):
    scheduleList = list(schedule.items())

    for event in scheduleList:
        eventName = event[0]
        eventTime, description = event[1]
        schedule.remove(eventName)
        scheduler.every().day.at(eventTime).do(sendNotify, eventName, description, schedule)

setUpSchedule(createSchedule())


while True:
    scheduler.run_pending()

import winsound
import datetime

alarm_hour = int(input("Enter hour: "))
alarm_minute = int(input("Enter minute: "))
alarmAmPm = input("AM or PM: ")

if alarmAmPm=="PM" or alarmAmPm=="pm":
    alarm_hour+=12

while True:
    if alarm_hour==datetime.datetime.now().hour and alarm_minute==datetime.datetime.now().minute:
        sound_play = True
        if alarm_hour>12:
            alarm_hour-=12
        print(f"Alarming at {alarm_hour}:{alarm_minute}")
        while sound_play:
            winsound.Beep(500,1000)
            stop_alarm = input("Do you wnat to stop the alarm,type 'stop' ")
            if stop_alarm=='stop' or stop_alarm=='STOP':
                sound_play = False
                break
        if sound_play == False:
            break
        


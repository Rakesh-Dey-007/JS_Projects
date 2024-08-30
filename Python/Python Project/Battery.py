# Battery Performance --->
import psutil

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%0d:%02d:%02d" % (hours, minutes, seconds)

battery = psutil.sensors_battery()
percent = battery.percent
time = convertTime(battery.secsleft)

print("Battery Percentage : ",percent)
print("Power Plugged in : ",battery.power_plugged)
print("Battery Left : ",time)
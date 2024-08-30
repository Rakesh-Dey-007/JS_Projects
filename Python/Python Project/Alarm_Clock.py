import datetime
import time
import pygame

def set_alarm(alarm_time, alarm_sound):
    pygame.mixer.init()  # Initialize the mixer module in pygame
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up! It's time to work!")
            pygame.mixer.music.load(alarm_sound)  # Load the alarm sound
            pygame.mixer.music.play()  # Play the sound
            while pygame.mixer.music.get_busy():  # Wait until the sound is done playing
                time.sleep(1)
            break
        time.sleep(1)  # Check the time every second

if __name__ == "__main__":
    alarm_time = input("Enter the time for the alarm (HH:MM format, 24-hour): ")
    alarm_sound = "Alarm_Tone.mp3"  # Replace with the path to your alarm sound file
    set_alarm(alarm_time, alarm_sound)

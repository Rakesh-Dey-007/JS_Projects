import pywhatkit

try:
    pywhatkit.sendwhatmsg("+91xxxxxxxxxx", 
                            "Hello\nHow are you.", 
                            22, 28)
    print("Successfully Sent!")

except:
    print("An Unexpected Error!")

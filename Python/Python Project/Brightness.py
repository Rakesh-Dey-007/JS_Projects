# Brightness increaser and decreaser.

import screen_brightness_control as bright

# Print current brightness levels
print("Current brightness level:", bright.get_brightness())

# Get the desired brightness level from the user
level = input("Enter Brightness Level (0-100): ")

# Set the new brightness level
bright.set_brightness(int(level))

# Print the new brightness levels
print("New brightness level:", bright.get_brightness())

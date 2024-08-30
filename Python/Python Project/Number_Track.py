# Number Track using Python --->

import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Input phone number
number = input("Enter a Phone Number with country code (e.g., +1234567890): ")

# Parse the phone number
phone = phonenumbers.parse(number)

# Get the timezone of the phone number
phone_timezones = timezone.time_zones_for_number(phone)

# Get the carrier of the phone number
phone_carrier = carrier.name_for_number(phone, "en")

# Get the geographical region of the phone number
phone_region = geocoder.description_for_number(phone, "en")

# Display the results
print(f"Phone Number: {phone}")
print(f"Timezones: {phone_timezones}")
print(f"Carrier: {phone_carrier}")
print(f"Region: {phone_region}")

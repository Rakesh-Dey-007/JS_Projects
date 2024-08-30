import phonenumbers
from phonenumbers import geocoder, carrier

# Example number for testing purposes
number = "+917001584784"

# Parse the number for the country and language
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

# Parse the number for the carrier and language
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

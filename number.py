import phonenumbers
from phonenumbers import timezone,geocoder,carrier

Number=input("Enter your Number with +91 : ")

parsed_number=phonenumbers.parse(Number)
time=timezone.time_zones_for_number(parsed_number)
place=geocoder.description_for_number(parsed_number,"en")
car=carrier.name_for_number(parsed_number, "en")


print(parsed_number)
print(time)
print(place)
print(car)

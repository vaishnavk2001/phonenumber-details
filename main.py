import phonenumbers
number = input("enter phone number:")

# for country #

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number,"CH")
print("country:",geocoder.description_for_number(ch_number,"en"))

# for service provider #

from phonenumbers import carrier
service_number = phonenumbers.parse(number,"RO")
print("SIM:",carrier.name_for_number(service_number,"en"))
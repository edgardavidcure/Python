
from calendar import month
from unicodedata import name


first_name = input ("\nEnter Your First Name: ").capitalize()
last_name = input ("Enter Your Last Name: ").upper()
email_address = input ("Enter Your Email Address: ").lower()
phone_number = input ("Enter Your Phone Number: ")
job_title = input ("Enter Your Job Title: ").title()
hair_color = input ("Enter Your Hair Color: ")
eye_color = input ("Enter Your Eye Color: ")
id_number = input ("Enter Your ID Number: ")
month = input ("Enter Your Start Month: ")
training = input ("Have you completed advanced training? 'Yes' or 'No': ")

print ("\nYour ID Card is:")
print ("----------------------------------------")
print (f"{last_name}, {first_name}")
print (f"{job_title}")
print (f"ID: {id_number}\n")
print (f"{email_address}")
print (f"{phone_number}")
print (f"Hair: {hair_color:<20} Eyes: {eye_color}")
print (f"Month: {month:<19} Training: {training}")
print ("----------------------------------------")

















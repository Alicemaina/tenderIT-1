import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tenderIT.settings')

import django
django.setup()

from TenderITApp.models import Company, Project, Rating, ProjectApplication

def populate():
    company1 = add_company('06382444', "IT SOLUTIONS LTD", "Canal View 2a",
                           "Chester", "United Kingdom", "CH3 6AN", "itsolutions@gmail.com",
                           "48853124568", "www.itsolutions.co.uk", "itsolutions", "it1234")
    company2 = add_company("04217916", "SKYSCANNER LIMITED", "Fore Street",
                           "London", "United Kingdom", "EC2Y 5EJ", "info@scyscanner.co.uk",
                           "44882156785", "www.skyscanner.co.uk", "skyscanner", "sky1234")
    company3 = add_company("SC327000", "Bank of Scotland", "The Mound", "Edinburgh", "United Kingdom", "EH1 1YZ", "info@bankofscotland.co.uk", "48573554897", "www.bankofscotland.co.uk", "bankofscotland", "bos1234")


    for c in Company.objects.all():
        print c

def add_company(nationalID, name, street, city, country, postcode, email, phone, website, username, password):
    c = Company.objects.get_or_create(nationalID=nationalID)[0]
    c.name = name
    c.street = street
    c.city = city
    c.country = country
    c.postcode = postcode
    c.email = email
    c.phone = phone
    c.website = website
    c.username = username
    c.password = password
    c.save()
    return c

if __name__ == '__main__':
   	print "Starting tender IT population script..."
   	populate()

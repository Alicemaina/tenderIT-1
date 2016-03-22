import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tenderIT.settings')

import django
django.setup()

from django.contrib import auth
from django.contrib.auth.models import User
from TenderITApp.models import Company, Project, Rating, ProjectApplication


def populate():
	user1 = add_user("leifos", "leifos")
	user2 = add_user("laura", "laura")
	user3 = add_user("david", "david")
	user4 = add_user("ismayil", "ismayil")
	user5 = add_user("devlogic", "dev1234")
	
	company1 = add_company(user1,"06382444", "IT SOLUTIONS LTD", "Canal View 2a", "Chester", "United Kingdom", "CH3 6AN", "itsolutions@gmail.com","48853124568", "www.itsolutions.co.uk")

	company2 = add_company(user2,"04217916", "SKYSCANNER LIMITED", "Fore Street","London", "United Kingdom", "EC2Y 5EJ", "info@scyscanner.co.uk","44882156785", "www.skyscanner.co.uk")

	company3 = add_company(user3,"SC327000", "Bank of Scotland", "The Mound", "Edinburgh","United Kingdom", "EH1 1YZ", "info@bankofscotland.co.uk", "48573554897", "www.bankofscotland.co.uk")

	company4 = add_company(user5,"4201193140009", "Devlogic D.O.O", "Kolodvorska 11a", "Sarajevo","Bosnia and Herzegovina", "71000", "info@devlogic.ba", "003873312346", "www.devlogic.ba")
	
	company5 = add_company(user4,"4", "Azerfon LLC", "H.Aliyev ave 106A", "Baku","Azerbaijan", "AZ1029", "info@nar.az", "00994124440777", "www.nar.az")

	company6 = add_company(user1,"AQWE972921883", "TMT LLC", "Dernegul ave 111", "Baku","Azerbaijan", "AZ1021", "info@tmt.az", "00994124423456", "www.tmt.az")

	company7 = add_company(user2,"CVFG972921883", "Bakcell LLC", "Neftciler ave 13", "Baku","Azerbaijan", "AZ1024", "info@bakcell.az", "00994124345673", "www.bakcell.az")

	company8 = add_company(user3,"BVCX972921883", "Azerconnect LLC", "28 May ave 6A", "Baku","Azerbaijan", "AZ1023", "info@azeconnect.az", "00994124212113", "www.azerconnect.az")

	company9 = add_company(user4,"RFVB972921883", "Azertelekom LLC", "Bul-Bul ave 1B", "Baku","Azerbaijan", "AZ1212", "info@azertelekom.az", "00994124657890", "www.azertelekom.az")

	company10 = add_company(user5,"QAZX972921883", "Nobel Oil LLC", "Z.Aliyeva ave 11A", "Baku","Azerbaijan", "AZ1456", "info@nobel-oil.az", "00994124543210", "www.nobel-oil.az")

	
	project1 = add_project(company1, "Web page development", "Develop a web page for our company_templates", 500000, 'USD', '2016-03-01', '2016-09-01', '2016-03-19' )

	project2 = add_project(company2, "ERP System add on", "Create an accouting add on for the existing ERP system. Add on needs to be able to connect to the employees github account and count the number of commits.", 100000, 'EUR', "2016-04-15", "2016-12-31", "2016-04-15")

	project3 = add_project(company3, "Azerbaijan Airlines API analyzer", "Develop an app that will connect to the Azerbaijan Airlines API and collect details about flights. App needs to organize collected information so that it can be used in our existing systems.", 80000,'GBP', "2016-05-01", "2016-08-30", "2016-05-01")

	project4 = add_project(company4, "Intranet developement", "Develop company intranet", 55000, 'USD', '2016-04-01', '2016-12-01', '2016-03-24' )

	project5 = add_project(company5, "Assets managmenent systems", "Provide assets management system to control all used equipments and available new equipments to replace with base station", 150000, 'EUR', "2016-04-25", "2016-12-31", "2016-04-15")

	project6 = add_project(company5, "TripOptimizer web application", "Develope one point access point for flight, tickets, hotels accomondation, and transport services", 86000,'GBP', "2016-05-01", "2016-08-30", "2016-04-21")
	
	project7 = add_project(company1, "Game management portal", "Develope portal for game environment settings and chosing suitable games", 54000, 'USD', '2016-06-01', '2016-09-01', '2016-05-19' )

	project8 = add_project(company2, "Railway simulator", "Create a simulator for a railway system", 10300, 'EUR', "2016-06-15", "2016-12-31", "2016-05-15")

	project9 = add_project(company4, "Lillybank Wine Merchant", "System to calculate sold, owed products and amounts", 85000,'GBP', "2016-07-01", "2016-08-30", "2016-06-01")
	
	add_application(project1, company4, 450000, "We would love to work on this project_templates.")
	add_application(project2, company3, 95960, "This project_templates looks really interesting, and we will dispatch our best team")
	add_application(project3, company5, 460000, "We will deliver the best solution.")
	add_application(project4, company4, 450000, "We would love to work on this project_templates.")
	add_application(project5, company2, 34000, "We will dedicate our best programmers to this project_templates and make sure we finish the necessary work in time.")
	add_application(project6, company1, 35600, "We will deliver the best solution.")
	add_application(project7, company4, 50000, "We would love to work on this project_templates.")
	add_application(project8, company1, 9500, "This project_templates looks really interesting. We will dedicate our best programmers to this project_templates and make sure we finish the necessary work in time.")
	add_application(project9, company2, 80000, "We will deliver  on time and the best solution .")

	add_rating(company1, company5, 5)
	add_rating(company2, company4, 4)
	add_rating(company4, company3, 5)
	add_rating(company3, company2, 2)
	add_rating(company5, company1, 5)
	add_rating(company1, company4, 5)
	add_rating(company2, company3, 4)
	add_rating(company4, company2, 5)
	add_rating(company3, company5, 2)
	add_rating(company5, company1, 5)
	add_rating(company1, company3, 5)
	add_rating(company2, company5, 4)
	add_rating(company4, company1, 5)
	add_rating(company3, company1, 2)
	add_rating(company5, company3, 5)

	for u in User.objects.all():
		print u
	for c in Company.objects.all():
		print c
	for p in Project.objects.all():
		print p
	for a in ProjectApplication.objects.all():
		print a
	for r in Rating.objects.all():
		print r
		
def add_user(username, password):
	u = User.objects.get_or_create(username=username)[0]
	u.username = username
	u.set_password(password)
	u.save()
	return u
		
def add_company(user, nationalID, name, street, city, country, postcode, email, phone, website):
	c = Company.objects.get_or_create(user=user)[0]
	c.nationalID = nationalID
	c.name = name
	c.street = street
	c.city = city
	c.country = country
	c.postcode = postcode
	c.email = email
	c.phone = phone
	c.website = website
	c.save()
	return c


def add_project(company, title, description, budget, currency, startDate, endDate, publishDate):
    p = Project.objects.get_or_create(company=company, title=title, budget=budget, currency=currency, startDate=startDate, endDate=endDate, publishDate=publishDate)[0]
    p.description = description
    p.save()
    return p

def add_application(project, applicant, price, description):
    a = ProjectApplication.objects.get_or_create(project=project, applicant=applicant, price=price)[0]
    a.description = description
    a.save()
    return a;

def add_rating(provider, receiver, value):
    r = Rating.objects.get_or_create(provider=provider, receiver=receiver, value=value)[0]
    r.save()
    return r

if __name__ == '__main__':
   	print "Starting tender IT population script..."
   	populate()

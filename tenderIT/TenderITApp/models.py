from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# from phonenumber_field.modelfields import PhoneNumberField

class Company(models.Model):
	user = models.OneToOneField(User)
	nationalID = models.CharField(max_length=64, validators=[MinLengthValidator(3)], unique=True)
	name = models.CharField(max_length=128, validators=[MinLengthValidator(3)])
	street = models.CharField(max_length=128)
	city = models.CharField(max_length=128)
	country = CountryField(countries_flag_url='flags/{ code }.png')
	postcode = models.CharField(max_length=16)
	email = models.EmailField()
	phone = models.CharField()
	phone = models.CharField(max_length=16)
	website = models.URLField()
	
	def __unicode__(self):
		return self.name

class Project(models.Model):
	company = models.ForeignKey(Company)
	title = models.CharField(max_length=128)
	description = models.TextField()
	budget = models.IntegerField()	
	DOLLAR = 'USD'
	EURO = 'EUR'
	POUND = 'GBP'
	CURRENCY_CHOICES = (
		(DOLLAR, 'US Dollar'),
		(EURO, 'Euro'),
		(POUND, 'British Pound'),
	)

	currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=DOLLAR)
	startDate = models.DateField()
	endDate = models.DateField()
	publishDate = models.DateField(auto_now_add=True)
	
	def __unicode__(self):
		return self.title

class Rating(models.Model):
	provider = models.ForeignKey(Company, related_name='rating_provider')
	receiver = models.ForeignKey(Company, related_name='rating_receiver')
	value = models.IntegerField(validators=[MaxValueValidator(5)])
	comment = models.TextField()	

	def __unicode__(self):
		return self.receiver.name + " - " + self.provider.name

class ProjectApplication(models.Model):
	project = models.ForeignKey(Project)
	applicant = models.ForeignKey(Company)
	price = models.IntegerField()
	description = models.TextField()

 	def __unicode__(self):
 		return self.project.title + " - " + self.applicant.name
	



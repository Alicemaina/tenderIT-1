from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MinLengthValidator, MaxValueValidator
from django_countries.fields import CountryField
from django.contrib.auth.models import User

class Company(models.Model):
	user = models.OneToOneField(User)
	nationalID = models.CharField(max_length=64, validators=[MinLengthValidator(3)], unique=True)
	name = models.CharField(max_length=128, validators=[MinLengthValidator(3)])
	street = models.CharField(max_length=128)
	city = models.CharField(max_length=128)
	country = CountryField()
	postcode = models.CharField(max_length=16)
	email = models.EmailField()
	phone = models.CharField(max_length=16)
	website = models.URLField()
	#username = models.CharField(max_length=16, validators=[MinLengthValidator(6)], unique=True)
	#password = models.CharField(max_length=12, validators=[MinLengthValidator(6)])	
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		#if self.id is None:
		self.slug = slugify(self.name)
		super(Company, self).save(*args, **kwargs)

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
	documents = models.FileField(upload_to='uploads/')	
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		if self.id is None:
			self.slug = slugify(self.title)
		super(Project, self).save(*args, **kwargs)

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
	



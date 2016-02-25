from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator, MaxValueValidator

class Company(models.Model):
	nationalID = models.CharField(max_length=64, unique=True)
	name = models.CharField(max_length=128)
	street = models.CharField(max_length=128)
	city = models.CharField(max_length=128)
	country = models.CharField(max_length=128)
	postcode = models.CharField(max_length=16)
	email = models.EmailField()
	phone = models.BigIntegerField()
	webiste = models.URLField()
	username = models.CharField(max_length=16, unique=True)
	password = models.CharField(max_length=12, validators=[RegexValidator(regex='^\w{6}$', message='Length has to be 6', code='nomatch')])	
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		if self.id is None:
			self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

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
		super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Rating(models.Model):
	provider = models.ForeignKey(Company, related_name='rating_provider')
	receiver = models.ForeignKey(Company, related_name='rating_receiver')
	value = models.IntegerField(validators=[MaxValueValidator(5)])
	comment = models.TextField()	

class ProjectApplication(models.Model):
	project = models.ForeignKey(Project)
	applicant = models.ForeignKey(Company)
	price = models.IntegerField()
	description = models.TextField()
	



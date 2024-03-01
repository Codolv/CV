from django.db import models


class Contact(models.Model):
	phone_number  = models.CharField(max_length=50)
	email_address = models.EmailField(max_length=50)
	home_page     = models.URLField(max_length=50)

	class Meta:
		db_table = "contact_informations"

	def __str__(self):
		return self.email_address


class Address(models.Model):
	street_name_with_house_number = models.CharField(max_length=100)
	zip_code = models.CharField(max_length=12)
	city     = models.CharField(max_length=50)
	country  = models.CharField(max_length=50, null=True)

	class Meta:
		db_table = "addresses"

	def __str__(self):
		return f"{self.city}, {self.country}"


class Person(models.Model):
	first_name      = models.CharField(max_length=50)
	last_name       = models.CharField(max_length=50)
	date_of_birth   = models.DateField()
	profile         = models.TextField()
	profile_picture = models.ImageField(upload_to='uploads/', null=True, blank=True)
	contact         = models.ForeignKey(Contact, on_delete=models.CASCADE)
	address         = models.ForeignKey(Address, on_delete=models.CASCADE)
	role            = models.CharField(max_length=50, null=True)

	class Meta:
		db_table = "persons"

	def __str__(self):
		return f"{self.first_name} {self.last_name}"


class Skill(models.Model):
	class Category(models.TextChoices):
		PROGRAMMING_LANGUAGE = "Programming Language"
		LANGUAGE             = "Language"
		TECHNOLOGY  		 = "Technology"
		FRAMEWORK   		 = "Framework"

	class Scale(models.IntegerChoices):
		BEGINNER = 1
		INTERMEDIATE = 2
		EXPERT = 3

	category = models.CharField(max_length=50, choices=Category.choices, default=Category.PROGRAMMING_LANGUAGE)
	name     = models.CharField(max_length=50)
	scale    = models.IntegerField(choices=Scale.choices, default=Scale.BEGINNER)
	person   = models.ForeignKey(Person, on_delete=models.CASCADE)

	class Meta:
		db_table = "skills"


class Education(models.Model):
	start_date  = models.DateField()
	end_date    = models.DateField(null=True)
	description = models.CharField(max_length=50)
	person      = models.ForeignKey(Person, on_delete=models.CASCADE)

	class Meta:
		db_table = "educations"

	def __str__(self):
		return self.description


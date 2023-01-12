from django.db import models

# Create your models here.
class contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=120)
	mobile=models.CharField(max_length=20)
	message=models.CharField(max_length=600)

	def __str__(self):
		return self.email
class category(models.Model):
	cname=models.CharField(max_length=30)
	cpic=models.ImageField(upload_to='static/category/',default="")
	cdate=models.DateField()

	def __str__(self):
		return self.cname

class profile(models.Model):
	name=models.CharField(max_length=120)
	mobile=models.CharField(max_length=20)
	email=models.CharField(max_length=80,primary_key=True)
	passwd=models.CharField(max_length=100)
	ppic=models.ImageField(upload_to='static/profile/',default="")
	address=models.TextField(max_length=2000)

class news(models.Model):
	city=models.CharField(max_length=200)
	headlines=models.CharField(max_length=400)
	subject=models.CharField(max_length=800)
	newsdes=models.TextField(max_length=8000)
	newspic=models.ImageField(upload_to='static/profile/',default="")
	ndate=models.DateField()
	ncategory=models.ForeignKey(category,on_delete=models.CASCADE)

class notification(models.Model):
	npic=models.ImageField(upload_to='static/notification/',default="")
	ndes=models.TextField(max_length=5000)
	ndate=models.DateField()


class video(models.Model):
	vtitle=models.CharField(max_length=200)
	vdes=models.TextField(max_length=600)
	thumb=models.ImageField(upload_to='static/thumbnail/',default="")
	vlink=models.CharField(max_length=500)
	vdate=models.DateField()

class slider(models.Model):
	stitle=models.CharField(max_length=200)
	sdes=models.CharField(max_length=500)
	spic=models.ImageField(upload_to='static/slider',default="")
	sdate=models.DateField()


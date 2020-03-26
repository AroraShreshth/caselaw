from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid 
# Create your models here.



class Categories(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

#Models for Cases
class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

class License(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)


class Case(models.Model):

    #Foreign KEy to User Model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    modified_date = models.DateTimeField(default=timezone.now)
    contribution_credit = models.NullBooleanField()
    consent = models.BooleanField()
    country = models.ForeignKey(Country)
    cc_license = models.ForeignKey(License, on_delete=models.PROTECT)
    jurisdiction = models.CharField(max_length=500, null=True, help_text="Within Country")
    court_name = models.CharField(max_length=500, help_text="Original and/or English Translation")
    decision_place = models.CharField(max_length=500, null=True)
    decision_date = models.DateTimeField(null=True) 
    link_decesion1 = models.URLField()
    link_decesion_eng_translated = models.URLField(null=True)
    background_info = models.TextField(max_length=5000, null=True)
    summary_decesion = models.TextField(max_length=5000, null=True)
    result_ruling = models.TextField(max_length=5000, null=True)
    implication = models.TextField(max_length=5000, null=True)
    categories = models.ManyToManyField(Categories)
    published = models.BooleanField(default=True)
class LinkCase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    type = models.CharField(max_length=100, ${blank=True, null=True})
    case = models.ForeignKey(Case)

#Scholarship Data Models
class Scholarship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CharField)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    modified_date = models.DateTimeField(default=timezone.now)
    contribution_credit = models.NullBooleanField()
    consent = models.BooleanField()
    country = models.ForeignKey(Country)
    title = models.CharField(max_length=500)
    publisher = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_published = models.DateTimeField()
    abstract = models.TextField(max_length=5000)
    category = models.ManyToManyField(Categories)

class LinkScholarship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    type = models.CharField(max_length=100, ${blank=True, null=True})
    case = models.ForeignKey(Scholarship)
    
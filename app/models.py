from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

import datetime


class Resume (models.Model):
    first_name      = models.CharField(max_length = 64, null = True)
    last_name       = models.CharField(max_length = 64, null = True)
    date_of_birth   = models.DateField(null = True)
    gender          = models.CharField(max_length = 16, null = True)
    marital_status  = models.CharField(max_length = 16, null = True)
    summary         = models.CharField(max_length = 2048, null = True)
    email           = models.EmailField(null = True)
    address         = models.CharField(max_length = 128, null = True)
    phone           = models.CharField(max_length = 32, null = True)
    skype           = models.CharField(max_length = 32, null = True)
    user            = models.ForeignKey(User)
    
    created_at      = models.DateTimeField(null = True, default = datetime.datetime.now)
    updated_at      = models.DateTimeField(null = True, default = datetime.datetime.now)
    
    @staticmethod
    def pre_save(sender, instance, *args, **kwargs):
        instance.updated_at = datetime.datetime.now()

#  --------------------------------------------------------------------------

class Skill (models.Model):
    title           = models.CharField(max_length = 32)
    score           = models.FloatField()
    resume          = models.ForeignKey(Resume)
    
    created_at      = models.DateTimeField(null = True, default = datetime.datetime.now)
    updated_at      = models.DateTimeField(null = True, default = datetime.datetime.now)
    
    @staticmethod
    def pre_save(sender, instance, *args, **kwargs):
        instance.updated_at = datetime.datetime.now()

#  --------------------------------------------------------------------------
    
class Experience (models.Model):
    title           = models.CharField(max_length = 128)
    desc            = models.CharField(max_length = 1024, null = True)
    duration        = models.CharField(max_length = 128, null = True)
    role            = models.CharField(max_length = 128, null = True)
    resume          = models.ForeignKey(Resume)
    
    created_at      = models.DateTimeField(null = True, default = datetime.datetime.now)
    updated_at      = models.DateTimeField(null = True, default = datetime.datetime.now)
    
    @staticmethod
    def pre_save(sender, instance, *args, **kwargs):
        instance.updated_at = datetime.datetime.now()
    
#  --------------------------------------------------------------------------
    
class Education (models.Model):
    institution     = models.CharField(max_length = 128)
    specialization  = models.CharField(max_length = 128)
    graduated_at    = models.DateField(null = True)
    resume          = models.ForeignKey(Resume)
    
    created_at      = models.DateTimeField(null = True, default = datetime.datetime.now)
    updated_at      = models.DateTimeField(null = True, default = datetime.datetime.now)
    
    @staticmethod
    def pre_save(sender, instance, *args, **kwargs):
        instance.updated_at = datetime.datetime.now()
    
#  --------------------------------------------------------------------------
    
class Language (models.Model):
    name            = models.CharField(max_length = 128)
    level           = models.CharField(max_length = 16)
    resume          = models.ForeignKey(Resume)
    
    created_at      = models.DateTimeField(null = True, default = datetime.datetime.now)
    updated_at      = models.DateTimeField(null = True, default = datetime.datetime.now)
    
    @staticmethod
    def pre_save(sender, instance, *args, **kwargs):
        instance.updated_at = datetime.datetime.now()

# hooks

pre_save.connect(Resume.pre_save, Resume)
pre_save.connect(Skill.pre_save, Skill)
pre_save.connect(Experience.pre_save, Experience)
pre_save.connect(Education.pre_save, Education)
pre_save.connect(Language.pre_save, Language)
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Team(models.Model):

    team_name = models.CharField(max_length=50, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    # yay for hardcode
    m1_full_name = models.CharField(max_length=50, blank=False)
    m1_school = models.CharField(max_length=50, blank=False)
    m1_course = models.CharField(max_length=50, blank=False)
    m1_contact_num = models.CharField(max_length=50, blank=False)
    m1_email = models.EmailField(max_length=50, blank=False)

    m2_full_name = models.CharField(max_length=50, blank=False)
    m2_school = models.CharField(max_length=50, blank=False)
    m2_course = models.CharField(max_length=50, blank=False)
    m2_contact_num = models.CharField(max_length=50, blank=False)
    m2_email = models.EmailField(max_length=50, blank=False)

    m3_full_name = models.CharField(max_length=50, blank=False)
    m3_school = models.CharField(max_length=50, blank=False)
    m3_course = models.CharField(max_length=50, blank=False)
    m3_contact_num = models.CharField(max_length=50, blank=False)
    m3_email = models.EmailField(max_length=50, blank=False)

    m4_full_name = models.CharField(max_length=50, blank=True, null=True)
    m4_school = models.CharField(max_length=50,  blank=True, null=True)
    m4_course = models.CharField(max_length=50,  blank=True, null=True)
    m4_contact_num = models.CharField(max_length=50,  blank=True, null=True)
    m4_email = models.EmailField(max_length=50,  blank=True, null=True)

    m5_full_name = models.CharField(max_length=50, blank=True, null=True)
    m5_school = models.CharField(max_length=50,  blank=True, null=True)
    m5_course = models.CharField(max_length=50,  blank=True, null=True)
    m5_contact_num = models.CharField(max_length=50,  blank=True, null=True)
    m5_email = models.EmailField(max_length=50,  blank=True, null=True)

    def __unicode__(self):
        return self.team_name

    def get_absolute_url(self):
        return reverse('home')


class Judge(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    organization = models.CharField(max_length=50, blank=False)
    picture = models.ImageField()
    description = models.TextField()

    def __unicode__(self):
        return self.full_name


class Sponsor(models.Model):
    CATEGORY_CHOICES = (
        ('Organizer', 'Organized by'),
        ('Transport', 'Official Transport Partner'),
        ('Platinum', 'Co-presented to by'),
        ('Gold', 'In Cooperation with'),
        ('Silver', 'Also brought to you by'),
        ('Bronze', 'Special thanks to'),
        ('Media', 'Media Sponsors'),
        ('Community', 'Community Partners'),
        ('Platinum Community Partner', 'Platinum Community Partner'),
        ('Gold Community Partner', 'Gold Community Partner'),
    )
    name = models.CharField(max_length=50, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    link = models.URLField(blank = True)
    picture = models.ImageField()

    def __unicode__(self):
        return self.name

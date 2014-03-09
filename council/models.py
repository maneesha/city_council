from django.db import models

# Create your models here.

class Councilperson(models.Model):
    first_name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 50, null = True, blank = True)
    last_name = models.CharField(max_length = 50)
    suffix = models.CharField(max_length = 10, null = True, blank = True)

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'M'), (FEMALE, 'F'))
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)

    race = models.CharField(max_length = 15, null = True, blank = True)
    birthdate = models.CharField(max_length = 10, null = True, blank = True)
    comments = models.TextField(null=True, blank = True)

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s' % (self.first_name, self.middle_name, self.last_name, self.suffix, self.gender, self.race, self.birthdate, self.comments)

class Term(models.Model):
    district = models.CharField(max_length = 8)
    DEMOCRAT = 'Democrat'
    REPUBLICAN = 'Republican'
    UNKNOWN = 'Unknown'
    PARTY_CHOICES = ((DEMOCRAT, 'Democrat'), (REPUBLICAN, 'Republican'), (UNKNOWN, 'Unknown'))

    party = models.CharField(max_length = 10, choices = PARTY_CHOICES, null=True, blank = True)

    start_date = models.CharField(max_length = 10, null = True, blank = True)
    end_date = models.CharField(max_length = 10, null = True, blank = True)

    RETIRED = 'retired'
    DEFEATED = 'defeated'
    RESIGNED = 'resigned'
    DIED = 'died'
    SCANDAL = 'scandal'
    UNKNOWN = 'unknown'
    HOW_LEFT_CHOICES = ((RETIRED, 'retired'), (DEFEATED, 'defeated'), (RESIGNED, 'resigned'), (DIED, 'died'), (SCANDAL, 'scandal'), (UNKNOWN, 'unknown'))
    
    departed = models.CharField(max_length = 25, choices = HOW_LEFT_CHOICES, null = True, blank = True)
    
    how_left_office = models.TextField(null=True, blank = True) 
    predecessor = models.ForeignKey(Councilperson, related_name = 'term_predecessor', null = True, blank = True)
    councilperson = models.ForeignKey(Councilperson)
    successor = models.ForeignKey(Councilperson, related_name = 'term_successor', null = True, blank = True)

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (self.district, self.party, self.start_date, self.end_date, self.how_left_office, self.councilperson, self.departed)

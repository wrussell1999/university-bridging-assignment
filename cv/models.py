from django.db import models

EDUCATION_TYPE_CHOICES = (
    ('school','Secondary School'),
    ('sixth_form', 'Sixth Form'),
    ('uni', 'University')
)

class Education(models.Model):
    institute = models.CharField(max_length=50)
    education_type = models.CharField(max_length=50, choices=EDUCATION_TYPE_CHOICES, default='University')
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    course = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.institute

class Experience(models.Model):
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.job_title

class Skill(models.Model):
    content = models.CharField(max_length=50)
    years_experience = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.content

class Project(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

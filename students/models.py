from django.db import models

# Create your models here.
class Students(models.Model):
    merit = models.IntegerField()
    score = models.IntegerField()
    enrollment = models.CharField(max_length=30)
    name = models.CharField(max_length=70)
    branch = models.CharField(max_length=90)
    year = models.CharField(max_length=90)
    gender = models.CharField(max_length=30)
    categeory = models.CharField(max_length=50)
    seattype = models.CharField(max_length=40)
    mobile_number = models.CharField(db_column='Mobile_Number', max_length=15)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=200)  # Field name made lowercase.
    registeration_number = models.CharField(db_column='Registeration_Number', max_length=200)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_Id', max_length=200)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'students'
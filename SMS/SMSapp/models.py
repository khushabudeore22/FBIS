from django.db import models

# Create your models here.
class StudentData(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    rollno=models.IntegerField()
    div=models.CharField(max_length=50)
    email=models.CharField(max_length=50 , unique=True,null=True, blank=True)
    review=models.TextField(blank=True,help_text="Give Your Feedback",default="No data provided")
    date=models.DateField(null=True,auto_now_add=True,blank=True)

    class Meta:
        db_table="StudentData"

    def __str__(self):
        return self.fname
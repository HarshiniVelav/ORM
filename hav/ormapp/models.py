from django.db import models
from django.contrib import admin
class Movies(models.Model):
    User_id = models.CharField(max_length=20, help_text="User ID")
    User_Name = models.CharField(max_length=100)
    email_id = models.EmailField()
    No_of_seats = models.IntegerField()
    Movie_Name=models.CharField(max_length=20)
    Show_DateTime=models.DateTimeField()
    Phone_Number=models.CharField(max_length=10, help_text="Phone number")
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('User_id', 'User_Name', 'email_id', 'No_of_seats', 'Movie_Name','Show_DateTime','Phone_Number')


from django.db import models

class Time(models.Model):
    t_count = models.IntegerField(db_column='count')
    t_currentTime = models.DateTimeField(db_column='currentTime')
    t_getAppTime = models.DateTimeField(db_column='getAppTime')
    class Meta():
        db_table = 'time'



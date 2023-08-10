from django.db import models

from django.db import models


class Move_Request(models.Model):
    DoesNotExist = None
    objects = None
    p_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    payscale = models.CharField(max_length=50)
    cnic_no = models.CharField(max_length=15)
    passport = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=15)
    project = models.CharField(max_length=50)
    time_of_move = models.CharField(max_length=10,
                                    choices=[('morning', 'Morning'), ('evening', 'Evening'), ('night', 'Night')])
    time_of_return = models.CharField(max_length=10,
                                      choices=[('morning', 'Morning'), ('evening', 'Evening'), ('night', 'Night')])
    mode_of_travel = models.CharField(max_length=10,
                                      choices=[('Air', 'Air'), ('Bus', 'Bus'), ('Road', 'Road'), ('Train', 'Train')])
    date_of_moves = models.DateField()
    date_of_return = models.DateField()
    route = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    category = models.CharField(max_length=20,
                                choices=[('Official', 'Official'), ('Private', 'Private'), ('Open', 'Open'),
                                         ('Classified', 'Classified')])
    pov = models.TextField()
    duration_days = models.IntegerField()
    duration_nights = models.IntegerField()
    relatedpro = models.CharField(max_length=50)
    fundingsources = models.TextField(blank=True)
    advance = models.CharField(max_length=5, choices=[('Yes', 'Yes'), ('No', 'No')])

    def __str__(self):
        return self.name

from django.db import models
from django.urls import reverse
# from datetime import date

METHODS = (
    ('S', 'Smudging'),
    ('W', 'Running Water'),
    ('M', 'Full Moon'),
    ('O', 'Other')
)


class Location(models.Model):
    place = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.place}'
    
    def get_absolute_url(self):
        return reverse('location_detail', kwargs={'pk': self.id})
        
class Crystal(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    hardness = models.IntegerField()
    color = models.CharField(max_length=100)
    location = models.ManyToManyField(Location)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'crystal_id': self.id})
    
    # def cleansed_for_the_month(self):
    #     return self.cleansing_set.filter(date=date.today()).count() >= 30

class Cleansing(models.Model):
    date = models.DateField('cleansing date')
    method = models.CharField(
        max_length=1,
        choices=METHODS,
        default=METHODS[0][0]
    )
    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_method_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
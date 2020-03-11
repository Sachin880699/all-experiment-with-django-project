from django.db import models


COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)


class Home(models.Model):
    name = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    image = models.ImageField(upload_to='Image')

    def __str__(self):
        return self.name

class form(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')


    def __str__(self):
        return self.name
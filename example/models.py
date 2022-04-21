from django.db import models

class Car(models.Model):
    Model_Choice = (
        (1,'Jeep'),
        (2,'Cabriolet'),
        (3,'Sedan'),
        (4,'Minivan'),
        (5,'Pick-Up')
    )
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=100,choices=Model_Choice)
    year = models.DateField(auto_now=False)
    color = models.CharField(max_length=100)
    price = models.BigIntegerField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
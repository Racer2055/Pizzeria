from django.db import models

# Create your models here.

class Pizza(models.Model):
    text = models.CharField(max_length = 200)

    def __str__(self):
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'
    
    def __str__(self):
        return f"{self.text[:50]}"

class Pizza_Image(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    pizza_img = models.ImageField(upload_to = 'images/')
    text = models.CharField(max_length = 200)

    class Meta:
        verbose_name_plural = 'Pizza Images'
    
    def __str__(self):
        return self.text
    
    
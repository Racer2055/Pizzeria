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

def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return f'images/{instance.text}.{extension}'

class Pizza_Image(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    text = models.CharField(max_length = 200)
    pizza_img = models.ImageField(upload_to = upload_location)
    

    class Meta:
        verbose_name_plural = 'Pizza Images'
    
    def __str__(self):
        return self.text

class Comment(models.Model):
   pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
   text = models.TextField()
   date_added = models.DateTimeField(auto_now_add = True)

   class Meta:
      verbose_name_plural = 'comments'
    
   def __str__(self):
      return f"{self.text[:50]}"
    
    
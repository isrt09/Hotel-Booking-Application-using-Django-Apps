from django.db import models

# Create your models here.
property_type = {
    ('s','Sale'),
    ('r','Rent')
}

class Property(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(choices=property_type, max_length=8)
    price = models.PositiveIntegerField()
    area = models.DecimalField(max_digits=8,decimal_places=2)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/',null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    

    


    

   
    



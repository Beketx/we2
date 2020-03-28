from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return '{}'.format(self.id)
    def to_json(self):
        return{
            'id':self.id,
            'name':self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default='1')
    description = models.TextField(default='')
    count = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.title)
    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'price':self.price,
            'description':self.description,
            'count':self.count,
            'category_id':self.category_id.id
        }




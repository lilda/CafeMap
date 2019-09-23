from django.db import models
from django.conf import settings

class Cafe(models.Model):
    title = models.CharField(max_length=100, blank=False)
    address = models.TextField()
    number = models.TextField()
    signature_menu = models.TextField()
    average_price = models.TextField()
    update_at = models.TimeField(auto_now=True)
    location = models.CharField(max_length=40)
    image = models.ImageField(upload_to="images/", blank=True)
    likes_count = models.IntegerField(default=0, null=False, blank=False, editable=False)

    def __str__ (self):
        return self.title

    def likes(self):
        return Cafe_Like.objects.filter(cafe=self)

    def unlikes(self):
        return Cafe_Unlike.objects.filter(cafe=self)
    
    def reviewses(self):
        return Review.objects.filter(cafe=self)

class Review(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name="review")
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)
    content = models.CharField(max_length=50, blank=True)
    likes_count = models.IntegerField(default=0, null=False, blank=False, editable=False)
    unlikes_count = models.IntegerField(default=0, null=False, blank=False, editable=False)

    def __str__(self):
        return self.content

    def likes(self):
        return Review_Like.objects.filter(review=self)

    def unlikes(self):
        return Review_Unlike.objects.filter(review=self)

class Cafe_Like(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name="like")

    def __str__(self):
        return self.cafe.title

class Cafe_Unlike(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name="unlike")

    def __str__(self):
        return self.cafe.title

class Review_Like(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="like")



class Review_Unlike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="unlike")



#    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Unlike",)
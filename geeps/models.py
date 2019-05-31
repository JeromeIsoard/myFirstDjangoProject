from django.db import models


# def getBuildingChoices():
#     buildings = Building.objects.all()
#     # make an array
#     buildings_array = []
#     # foreach buildings add building name in the array
#     for b in buildings:
#         buildings_array.append(b.get_name_display())
#     return buildings_array


class PrintingRequest(models.Model):
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    # date = models.DateTimeField(default=timezone.now)
    # building = models.CharField(choices=getBuildingChoices())


class Building(models.Model):
    name = models.CharField(max_length=50)

# class Post(models.Model):
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#         default=timezone.now)
#     published_date = models.DateTimeField(
#         blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title

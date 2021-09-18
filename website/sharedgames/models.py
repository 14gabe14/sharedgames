from django.contrib.auth.models import User
from django.db import models
import uuid

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_multiplayer = models.BooleanField()

#games that are multiplayer database
class Multiplayer(models.Model):
    id = models.OneToOneField(Game, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    header_image = models.URLField(max_length = 200)
    is_free = models.BooleanField()
    rating = models.FloatField()

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    steam_id = models.IntegerField(unique=True)
    friends = models.ManyToManyField('self')

class Collection(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Multiplayer, on_delete=models.CASCADE)
    rating = models.FloatField()
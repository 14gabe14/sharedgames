from django.contrib import admin
from .models import Game, Multiplayer, Player, Collection

admin.site.register(Game)
admin.site.register(Multiplayer)
admin.site.register(Player)
admin.site.register(Collection)
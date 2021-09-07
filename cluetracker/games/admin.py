from django.contrib import admin
from games.models import (Game, Player, Card, Have, Pass, Show)

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Card)
admin.site.register(Have)
admin.site.register(Pass)
admin.site.register(Show)

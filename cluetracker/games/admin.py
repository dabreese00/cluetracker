from django.contrib import admin
from games.models import (Game, Player, Card, PersonCard, WeaponCard, RoomCard,
                          Have, Pass, Show)

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Card)
admin.site.register(PersonCard)
admin.site.register(WeaponCard)
admin.site.register(RoomCard)
admin.site.register(Have)
admin.site.register(Pass)
admin.site.register(Show)

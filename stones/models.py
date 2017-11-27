from django.db import models

from players.models import Player

class Stone(models.Model):
    stone_id = models.IntegerField('Stone ID', primary_key = True)
    name = models.CharField('Stone name', max_length = 255, default = '')

    def __str__(self):
        return self.name

STONE_ACCESS_TYPES = (
        ('0', 'Denied'),
        ('1', 'Granted'),
        ('2', 'Lockpickable'),
        )
class Access(models.Model):
    stone = models.ForeignKey(Stone, on_delete = models.PROTECT)
    player = models.ForeignKey(Player, on_delete = models.PROTECT)
    access_type = models.CharField('Access type', max_length = 1, choices = STONE_ACCESS_TYPES)

    def access_type_str(self):
        if self.access_type:
            return dict(STONE_ACCESS_TYPES)[self.access_type]
        return None

    def __str__(self):
        return "Access to {} for {} is {}".format(self.stone, self.player, self.access_type_str())


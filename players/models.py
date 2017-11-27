from django.db import models

class Player(models.Model):
    pid = models.IntegerField('Player ID', primary_key = True)
    name = models.CharField('Player name', max_length = 255, default = '')
    rfid = models.IntegerField('RFID tag')

    def __str__(self):
        return 'Player {}'.format(self.pid)


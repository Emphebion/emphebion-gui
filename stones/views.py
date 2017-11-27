from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Stone, STONE_ACCESS_TYPES, Player, Access

from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key): return dictionary.get(key)

def index(request):
    stones_list = Stone.objects.order_by('name')
    context = {
        'stones_list': stones_list,
    }
    return render(request, 'stones/stones_list.html', context)

def stone_detail(request, stone_id):
    stone = get_object_or_404(Stone, pk = stone_id)
    players_list = Player.objects.order_by('name')
    accesses = {p.pid: ((Access.objects.get_or_create(stone = stone, player = p))[0].access_type) for p in players_list}
    print(accesses)
    return render(request, 'stones/stone.html', {'stone': stone, 'players_list': players_list, 'accesses': accesses, 'access_types': dict(STONE_ACCESS_TYPES)})

def stone_mod_access(request, stone_id):
    stone = get_object_or_404(Stone, pk = stone_id)
    players_list = Player.objects.all()
    for player in players_list:
        new_access = request.POST['access{}'.format(player.pid)]
        access, _ = Access.objects.get_or_create(stone = stone, player = player)
        access.access_type = new_access
        access.save()

    return HttpResponseRedirect(reverse('stones:stone_detail', args=(stone.stone_id,)))

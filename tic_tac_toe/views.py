from django.shortcuts import render, redirect
from .models import Game
from django.contrib import messages

# Create your views here.



def home(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        option = request.POST.get('option')
        room_code = request.POST.get('room_code')
        if str(option) == '1':
            game_obj = Game.objects.filter(room_code = room_code).first()
            if game_obj is None:
                messages.success(request, 'Room Code Does Not Found')
                return redirect('/')
            
            if game_obj.is_over:
                messages.success(request, 'Game Is Over , Please Create New Game')
                return redirect('/')

            game_obj.game_opponent = username
            game_obj.save()
        else :
            game_obj = Game.objects.create(
                room_code = room_code,
                game_creator = username,
            )
            game_obj.save()
        return redirect('/play/'+room_code + '?username='+username)


    return render(request, 'home.html')



def play(request, room_code):
    username = request.GET.get('username')
    first_turn = Game.objects.filter(room_code = room_code).first()
    print(first_turn)
    first_turn = first_turn.game_creator
    print(first_turn)
    context = {
        'username':username,
        'room_code':room_code,
        'first_turn':first_turn,
    }
    return render(request, 'play.html', context)



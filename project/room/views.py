from django.shortcuts import render
from .models import Room, Message

# View for the rooms
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'core/rooms.html', {'rooms': rooms})

def room(request, pk):
    room = Room.objects.get(pk=pk)
    # Get the messages from the database
    messages = Message.objects.filter(room=room)[0:25]

    # Add the messages to the context
    #'messages': messages


    return render(request, 'core/room.html', {'room': room, 'messages': messages})


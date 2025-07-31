from django.shortcuts import render

def home(request):
    return render(request, 'booking_room/home.html')

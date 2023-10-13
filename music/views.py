from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.http import HttpResponse
from . models import Music

# Create your views here.
def index(request):
    music = Music.objects.all().order_by('title')
    music_list = list(Music.objects.all().order_by('title').values())
    return render(request, 'home.html', {'musics': music, 'music_list': music_list})

def add(request):
    if(request.method == "POST"):
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        audio = request.FILES.get('audio_file')
        image = request.FILES.get('cover_image')
        lyric = request.POST.get('lyrics')
        
        data = Music.objects.create(
            title=title, artist=artist, audio_file=audio, cover_image=image, lyrics=lyric
            # 
        )
        data.save()
        return redirect('music:home')
    return render(request, 'add.html')

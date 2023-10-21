from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.http import HttpResponse
from PyDictionary import PyDictionary
from . models import Music

# Create your views here.
def main(request):
    music = Music.objects.all().order_by('title')
    music_list = list(Music.objects.all().order_by('title').values())
    return render(request, 'main.html', {'musics': music, 'music_list': music_list})

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
        vocab = request.POST.get('vocabulary')
        # Vocab = request.POST.get('vocab')
        
        data = Music.objects.create(
            title=title, artist=artist, audio_file=audio, cover_image=image, lyrics=lyric, vocabulary=vocab
            # , Vocab = Vocab
        )
        data.save()
        return redirect('music:home')
    return render(request, 'add.html')

def vocabulary(request):
    # vocab = Music.objects.all().order_by('eng')
    # vocab_example = Music.objects.all().order_by('eng').values('eng', 'meaning')
    music = Music.objects.all().order_by('title')
    music_list = list(Music.objects.all().order_by('title').values())
    # return render(request, 'vocab.html', {'vocabs':vocab,'vocab_example': vocab_example,'musics': music, 'music_list': music_list })
    return render(request, 'vocab.html', {'musics': music, 'music_list': music_list })


def dict(request):
    return render(request, 'dict.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    context = {
        'meaning': dictionary.meaning(search)['Noun'][0],
        'symnonyms': dictionary.synonym(search),
        'antonyms': dictionary.antonym(search)
    }
    return render(request, 'word.html')

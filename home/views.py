import random

from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from .models import Single, Album

def _404(request):
    return render(request, 'home/404.html')

def index(request):
    works = [{'typ' : 'single', 'song' : i} for i in Single.objects.all()]
    works += [{'typ' : 'album', 'song' : i} for i in Album.objects.all()]

    random.shuffle(works, lambda: random.random() )
    # works = works[:4]

    track_list = [{'title' : i.title, 'path': i.songFile.url, 'coverPhoto' : i.coverPhoto.url, 'author' : i.author.penName} for i in Single.objects.all()]
    random.shuffle(track_list, lambda: random.random() )

    return render(request, 'home/index.html', {'works' : works, 'track_list' : track_list})

def songView(request, typ, pk):
    if(typ == 'album'):

        try:
            work_model = Album.objects.get(pk = pk)
        except Album.DoesNotExist:
            raise Http404("Album doesn't exist")

        author = work_model.author.name

        singles_by_author = Single.objects.filter(author=work_model.author)
        albums_by_author = Album.objects.filter(author=work_model.author)

        works = [{'typ' : 'single', 'song' : i} for i in singles_by_author]
        works += [{'typ' : 'album', 'song' : i} for i in albums_by_author]

        random.shuffle(works, lambda: random.random())
        # works = works[:4]


        track_list = []

        songs_in_album = []
        artists = set()
        loop_index = 1
        for single in work_model.songs.all():
            collabs = []
            for collab in single.collabs.all():
                collabs.append(collab.penName)
                artists.add(collab)

            songs_in_album.append({
                'index' : loop_index,
                'title' : single.title,
                'artists' : [author] + collabs,
            })

            track_list.append(
                {'title' : single.title, 'path': single.songFile.url, 'coverPhoto' : single.coverPhoto.url, 'author' : single.author.penName}
            )

            loop_index += 1

        work = {
            'coverPhoto' : work_model.coverPhoto.url,
            'author' : author,
            'genre' : work_model.genre,
            'release_year' : work_model.release_year,
            'title' : work_model.title,
            'songs' : songs_in_album,
            'artists' : [work_model.author] + list(artists)
        }

        return render(
            request,
            'home/single_details.html',
            {
                'work' : work,
                'track_list' : track_list,
                'more_like_this' : works,
            }
        )
    elif(typ == 'single'):
        try:
            work_model = Single.objects.get(pk = pk)
        except Single.DoesNotExist:
            raise Http404("Album doesn't exist")

        author = work_model.author.name

        singles_by_author = Single.objects.filter(author=work_model.author)
        albums_by_author = Album.objects.filter(author=work_model.author)

        works = [{'typ' : 'single', 'song' : i} for i in singles_by_author]
        works += [{'typ' : 'album', 'song' : i} for i in albums_by_author]

        random.shuffle(works, lambda: random.random())
        # works = works[:4]


        track_list = []

        songs_in_album = []
        artists = set()
        loop_index = 1
        for single in [work_model]:
            collabs = []
            for collab in single.collabs.all():
                collabs.append(collab.penName)
                artists.add(collab)

            songs_in_album.append({
                'index' : loop_index,
                'title' : single.title,
                'artists' : [author] + collabs,
            })

            track_list.append(
                {'title' : single.title, 'path': single.songFile.url, 'coverPhoto' : single.coverPhoto.url, 'author' : single.author.penName}
            )

            loop_index += 1

        work = {
            'coverPhoto' : work_model.coverPhoto.url,
            'author' : author,
            'genre' : work_model.genre,
            'release_year' : work_model.release_year,
            'title' : work_model.title,
            'songs' : songs_in_album,
            'artists' : [work_model.author] + list(artists)
        }
        
        return render(
            request,
            'home/single_details.html',
            {
                'work' : work,
                'track_list' : track_list,
                'more_like_this' : works,
            }
        )

    else:
        return Http404("Page not Found!")
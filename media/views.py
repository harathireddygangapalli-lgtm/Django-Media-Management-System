from django.shortcuts import render, redirect
from .models import Media


def upload_media(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')

        if title and file:
            Media.objects.create(title=title, file=file)
            return redirect('upload_media')

    return render(request, 'upload.html')


def gallery(request):
    media_files = Media.objects.all()
    return render(request, 'gallery.html', {'media_files': media_files})


def delete_media(request, id):
    media = Media.objects.get(id=id)

    if request.method == 'POST':
        media.file.delete()
        media.delete()
        return redirect('gallery')

    return render(request, 'delete.html', {'media': media})


def edit_media(request, id):
    media = Media.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')

        media.title = title

        if file:
            media.file.delete()
            media.file = file

        media.save()

        return redirect('gallery')

    return render(request, 'edit.html', {'media': media})
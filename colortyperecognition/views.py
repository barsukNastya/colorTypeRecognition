from django.shortcuts import render, get_object_or_404
from .models import Photo, HairColor
from .forms import UploadFileForm
from pprint import pprint
from inspect import getmembers
from django.http import HttpResponseRedirect

def greating(request):
  hair_colors = HairColor.objects.all()

  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      instance = Photo(file_field=request.FILES['file'])
      instance.save()
      # return HttpResponseRedirect('/success/url/')
  else:
    form = UploadFileForm()

  return render(request, 'colortyperecognition/greating.html', {'hair_colors' : hair_colors, 'request': request, 'form' : form})


def hair_color_detail(request, pk):
  post = get_object_or_404(HairColor, pk=pk)
  return render(request, 'colortyperecognition/hair_color_detail.html', {'post': post})


# def upload_file(request):
#   if request.method == 'POST':
#     form = UploadFileForm(request.POST, request.FILES)
#     if form.is_valid():
#       instance = Photo(file_field=request.FILES['file'])
#       instance.save()
#       return HttpResponseRedirect('/success/url/')
#   else:
#     form = UploadFileForm()
#   return render(request, 'colortyperecognition/greating.html', {'form': form})

  # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')s
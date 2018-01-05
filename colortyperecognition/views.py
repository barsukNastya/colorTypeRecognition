from django.shortcuts import render
from .models import HairColor

def greating(request):
  hair_colors = HairColor.objects.all()
  return render(request, 'colortyperecognition/greating.html', {'hair_colors' : hair_colors})

  # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
from django.shortcuts import render

def greating(request):
  return render(request, 'colortyperecognition/greating.html', {})
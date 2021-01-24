from django.shortcuts import render

# Create your views here.
def samplefunc(request):
    return render(request, 'sample.html',{})
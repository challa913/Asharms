from django.shortcuts import render, render_to_response

# Create your views here.

def sample_html(request):
    return render_to_response('home.html')
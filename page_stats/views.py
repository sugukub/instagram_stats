from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import instagram_page_stats

# Create your views here.
def home_page(request):
    if request.method == "POST":
        if request.POST.get("get_links"):    
            
            input_links = request.POST.get("links")
            username = request.POST.get("username")
            password = request.POST.get("password")

            page_stats = instagram_page_stats.main_program(input_links, username, password)
            return render(request, "Instagram_page_stats/display_page_stats.html", {
                'page_stats':page_stats
            } ) 

    elif request.method == "GET":
        request.session['audio_index'] = "testing"
        return render(request, "Instagram_page_stats/home_page.html", {})
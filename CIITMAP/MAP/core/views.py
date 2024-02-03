from django.shortcuts import render
from django.http import HttpResponse
import os

 #All codes here is only for the main page
# Create your views here.         
#             ____||____
#            ///////////\
#           ///////////  \
#           |    _    |  |
#           |[] | | []|[]|
#           |   | |   |  |home
def home(request):
    return render(request, 'Main Page.html')

#            _.-"\
#        _.-"     \
#     ,-"          \
#    ( \            \
#     \ \            \
#      \ \            \
#       \ \         _.-;
#        \ \    _.-"   :
#         \ \,-"    _.-"
#          \(   _.-"  
#           `--" about
def about(request):
    return render(request, 'About Us.html')

def back(request):
    return render(request, 'Main Page.html')

#====================================================#



#We call all path inside of Explore
#All codes here is only for Explore

#             .-""-.
#     _______/      \  
#    |_______        ;
#            \      /
#             '-..-'explore
def explore(request):                          
    return render(request, 'Explore.html') 

   #This is for all floors

def floor1(request):
    return render(request, 'Floor 1.html')

def floor2(request):
    return render(request, 'Floor 2.html')

def floor3(request):
    return render(request, 'Floor 3.html')

def floor4(request):
    return render(request, 'Floor 4.html')

def floor5(request):
    return render(request, 'Floor 5.html')

def floor6(request):
    return render(request, 'Floor 6.html')

def floor7(request):
    return render(request, 'Floor 7.html')

def overview(request):
    return render(request, 'Overview.html')

    #======================================================================


def backEx(request):
    return render(request, 'Explore.html')


#ABOUT US
def tripolca(request):
    return render(request, 'Tripolca Page.html')

def ador(request):
    return render(request,'Ador Page.html')

def maravilla(request):
    return render(request, 'Maravilla Page.html')







   







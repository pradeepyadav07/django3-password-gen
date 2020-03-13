from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html' )

def password(request):
    thepassword = 'testing'
    characters =list('fghmklfgjlkfdsgtufjfjhgqqqqwerwetyuiiouiopadsfghjkmnbvcxz')
    length= int(request.GET.get('Length',14))
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTGYHIJHGFDSZXCVBN'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})
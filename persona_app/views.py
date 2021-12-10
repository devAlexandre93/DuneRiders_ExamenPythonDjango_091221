from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import html
from .models import Persona
import requests

# Create your views here.

def home(request):
    return render(request, 'persona_app/home.html') 

def persona_list(request):
    personas = Persona.objects.all().order_by('-id')
    context = {
        'personas':personas
    }
    return render(request, 'persona_app/persona_list.html', context)    

def persona_details(request, id):
    persona = Persona.objects.get(id=id)
    context = {
        'persona':persona
    }
    return render(request, 'persona_app/persona_details.html', context)

def persona_generate(request):
    data = requests.get('https://randomuser.me/api?nat=fr').json()
    first_name = data['results'][0]['name']['first']
    print(first_name)
    last_name = data['results'][0]['name']['last']
    print(last_name)
    address_street = data['results'][0]['location']['street']['name']
    print(address_street)
    address_number = data['results'][0]['location']['street']['number']
    print(address_number)
    city = data['results'][0]['location']['city']
    print(city)
    country = data['results'][0]['location']['country']
    print(country)
    postcode = data['results'][0]['location']['postcode']
    print(postcode)
    email = data['results'][0]['email']
    print(email)
    username = data['results'][0]['login']['username']
    print(username)
    password = data['results'][0]['login']['password']
    print(password)
    age = data['results'][0]['registered']['age']
    print(age)
    picture = data['results'][0]['picture']['medium']
    print(picture)
    # Persona.objects.__new__(Persona)
    return HttpResponse(f'Generate persona')
    #return redirect('persona_details' persona.id)
    #return render(request, 'persona_app/persona_details.html', context)

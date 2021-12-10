from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import html
from requests.api import post
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
    # Add variables to get datas from the randomuserapi
    first_name = data['results'][0]['name']['first']
    last_name = data['results'][0]['name']['last']
    address_street = data['results'][0]['location']['street']['name']
    address_number = data['results'][0]['location']['street']['number']
    city = data['results'][0]['location']['city']
    country = data['results'][0]['location']['country']
    postcode = data['results'][0]['location']['postcode']
    email = data['results'][0]['email']
    username = data['results'][0]['login']['username']
    password = data['results'][0]['login']['password']
    age = data['results'][0]['registered']['age']
    picture = data['results'][0]['picture']['medium']
    # Generate the persona
    new_Persona = Persona(
       first_name = first_name,
       last_name = last_name,
       address_street = address_street,
       address_number = address_number,
       city = city,
       country = country,
       postcode = postcode,
       email = email,
       username = username,
       password = password,
       age = age,
       picture = picture
    )
    # Save the persona in the database
    new_Persona.save()
    # Redirect to the page persona_details of the new persona
    return redirect('persona_details', new_Persona.id)

def persona_delete(request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    return redirect('persona_list')

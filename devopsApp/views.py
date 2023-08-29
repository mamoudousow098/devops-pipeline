from django.shortcuts import render
from .models import Person

# Create your views here.

users = [ 
    {
    "firstname" : "mamoudou",
    "lastname" : "ousmane",
    "username" : "ousmane45" ,
    "email" : "ousmane45@gmail.com"
    },
    
     {
    "firstname" : "penda",
    "lastname" : "sall",
    "username" : "spenda10" ,
    "email" : "penda45@gmail.com"
    },
      {
    "firstname" : "coumba",
    "lastname" : "fall",
    "username" : "fcoumba" ,
    "email" : "coumbis@gmail.ocm"
    },
     {
    "firstname" : "demba",
    "lastname" : "ly",
    "username" : "lydem89" ,
    "email" : "lydem89@gmail.com"
    }
]
    


def home_view(request, *args, **kwargs):
    
    people = Person.objects.all()
    if people :
        return render(request, 'home.html', { 'people': people} )
    
    else :
        for user in users :
            person = Person(firstname = user['firstname'], 
                            lastname=user['lastname'],
                            email = user['email'],
                            username = user['username'])
            
            person.save()
        
    people = Person.objects.all()
    
    return render(request, 'home.html', { 'people': people} )
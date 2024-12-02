from django.shortcuts import render

# Create your views here.

def home(request):
     data={
        'name':"Bimal BK",
        'description':"I love coding, i'm looking for startup company where i can put efforts on it"
        }
     return render(request,'base/home.html',context=data)





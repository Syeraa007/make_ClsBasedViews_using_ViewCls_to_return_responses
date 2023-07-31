from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView

# Function Based Views to return string and Html page as responses

def fbv_string(request):
    return HttpResponse("<center><h1>This is FBV's string response</h1></center>")

def fbv_html(request):
    return render(request,'fbv_html.html')
 
# Function Based Views to return string and Html page as responses

class Cbv_string(View):
    def get(self,request):
        return HttpResponse("<center><h1>This is CBV's string response</h1></center>")
    
class Cbv_html(View):
    def get(self,request):
        return render(request,'Cbv_html.html')
    
class Cbv_template(TemplateView):
    template_name='Cbv_template.html'
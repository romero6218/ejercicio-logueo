from django.shortcuts import render
from django.views import generic
import requests

# Create your views here.
class login(generic.TemplateView):
    template_name = "login.html"
    def post(self, request, *args, **kwargs):
        a = requests.post("https://warm-oasis-29730.herokuapp.com/log-in/",
                          data={"username":request.POST["user"], "password":request.POST["password"]})
        context = {}
        context['status'] = a.content
        return self.render_to_response(context)

class signup(generic.TemplateView):
    template_name = "login.html"
    def post(self, request, *args, **kwargs):
        a = requests.post("https://warm-oasis-29730.herokuapp.com/log-in/",
                          data={"user":request.POST, "password":request.POST})
        context = {}
        context['status'] = a.content
        return self.render_to_response(context)


from django.shortcuts import render

# Create your views here.
from django.views import View
from . import models


class IndexView(View):
    def get(self, request):
        all_site = models.Allsite.objects.all()

        return render(request, "index.html", context={"all_site": all_site})


class HelpInfoView(View):
    def get(self, request):
        return render(request, "help.html")



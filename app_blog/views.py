from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        articles = Article.objects.all()
        return render(request, 'index.html', context={'articles': articles})
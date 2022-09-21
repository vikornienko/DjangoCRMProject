from django.shortcuts import render

from .models import Lead

def home_page(request):
    leads = Lead.objects.all()
    context_for_page = {
        'leads': leads
    }
    return render(request, 'leads/home_page.html', context_for_page)

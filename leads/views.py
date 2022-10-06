from django.http import HttpResponse
from django.shortcuts import render

from .models import Lead

def lead_list(request):
    leads = Lead.objects.all()
    context_for_page = {
        'leads': leads
    }
    return render(request, 'leads/lead_list.html', context_for_page)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context_for_page = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context_for_page)
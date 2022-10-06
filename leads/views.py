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
    return HttpResponse(f'here is the lead number {lead} detail view')
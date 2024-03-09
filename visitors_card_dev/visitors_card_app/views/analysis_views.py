from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def list_company(request):
    return render(request, 'visitors_card_app/analysis/list_company.html')

@login_required
def list_name(request):
    return render(request, 'visitors_card_app/analysis/list_name.html')

@login_required
def list_interviewer(request):
    return render(request, 'visitors_card_app/analysis/list_interviewer.html')

@login_required
def list_history(request):
    return render(request, 'visitors_card_app/analysis/list_history.html')

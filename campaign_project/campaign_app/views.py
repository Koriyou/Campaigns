# Campaign_Manager/campaign_app/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'campaign_app/index.html')

# Define more views as needed

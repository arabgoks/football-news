from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406437451',
        'name': 'Muhammad Hafizh',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
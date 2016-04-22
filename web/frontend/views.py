from django.shortcuts import render


# Create your views here.
def index_view(request):
    print(150)
    return render(request, 'index.html')

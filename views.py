from django.shortcuts import render

# Create your views here.
def add_show(request):
    return render(request, 'enroll/addandshow.html')

# def index_show(request):
#     return render(request, 'enroll/index.html')
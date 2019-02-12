from django.shortcuts import render, HttpResponse

def home_view(request):
    if request.user.is_authenticated():
        name = request.user.first_name
        fullname = request.user.get_full_name()
        context = {
            'name' : fullname
        }
    else:
        context = {
            'name': 'Misafir'
        }

    return render(request, 'home.html', context)

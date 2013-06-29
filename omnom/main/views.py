from django.http import HttpResponse

def temp_page(request):
    return HttpResponse(request.user.username)

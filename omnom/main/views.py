from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def test_page(request):
    return render_to_response("test-page.html",{'myvar':"OMNOM"},RequestContext(request))

def actions_fulfill_request(request,request_id):
    return HttpResponse("Fulfill Request Endpoint")

def actions_confirm_request(request,request_id):
    return HttpResponse("Confirm Request Endpoint")

def actions_pickup_request(request,request_id):
    return HttpResponse("Pickup Request Endpoint")

def home(request):
	  return render_to_response("home.html")

def donation_map(request):
	  return render_to_response("donation_map.html")

def requests(request):
	return render_to_response("requests.html")

def get_pic_url(request):
    picurl = "https://graph.facebook.com/%s/picture" % request.user.username
    return render_to_response("person.html", {'picurl':picurl})

def msg_confirmation(request):
	  return render_to_response("msg_confirmation.html")

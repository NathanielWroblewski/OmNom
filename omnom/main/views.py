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

def requests(request):
	  return render_to_response("requests.html")

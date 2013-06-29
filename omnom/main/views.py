from django.http import HttpResponse

def actions_fulfill_request(request,request_id):
    return HttpResponse("Fulfill Request Endpoint")

def actions_confirm_request(request,request_id):
    return HttpResponse("Confirm Request Endpoint")

def actions_pickup_request(request,request_id):
    return HttpResponse("Pickup Request Endpoint")

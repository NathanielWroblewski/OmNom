from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from twilio.rest import TwilioRestClient
from django.conf import settings
from main.models import PickupRequest

def create_pickup_request(request):
    if request.method=="POST":
        new_request = PickupRequest(
            description = request.POST.get("description",""),
            latitude=request.POST.get("latitude",0),
            longitude=request.POST.get("longitude",0),
            requester=request.user
        )
        new_request.save()

    all_requests = PickupRequest.objects.all();

    return render_to_response("create_request.html",{'all_requests':all_requests},RequestContext(request))
                  

def test_page(request):
    return render_to_response("test-page.html",{'myvar':"OMNOM"},RequestContext(request))

def actions_fulfill_request(request,request_id):
    return HttpResponse("Fulfill Request Endpoint")

def actions_confirm_request(request,request_id):
    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.sms.messages.create(to="+14154252139", from_="+17202599396", body="Test")
    return HttpResponse("Confirm Request Endpoint")

def twilio_callback(request):
    print "model hit"
    print request.GET
    body = request.GET.getlist("Body")
    from_ = request.GET.getlist("From")
    print body
    return HttpResponse("Twilio Callback")

def actions_pickup_request(request,request_id):
    return HttpResponse("Pickup Request Endpoint")

def home(request):
	return render_to_response("home.html",RequestContext(request))

def donation_map(request):
	return render_to_response("donation_map.html",RequestContext(request))

def requests(request):
	return render_to_response("requests.html",RequestContext(request))

def get_pic_url(request):
    picurl = "https://graph.facebook.com/%s/picture" % request.user.username
    return render_to_response("person.html", {'picurl':picurl})

def msg_confirmation(request):
	return render_to_response("msg_confirmation.html",RequestContext(request))

def direction_map(request):
    return render_to_response("direction_map.html",RequestContext(request))

def feedback(request):
    return render_to_response("feedback.html",RequestContext(request))

def picked_up(request):
    return render_to_response("picked_up.html",RequestContext(request))

def sign_in(request):
    return render_to_response("sign_in.html",RequestContext(request))

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from twilio.rest import TwilioRestClient
from django.conf import settings
from main.models import *
from django.shortcuts import redirect

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
    # try
    #     pickup_request = PickupRequest.objects.get(id=request_id)
    #     donnor_phone_number = pickup_request.requester.user_profile.phone_number
    #     volunteer = request.user
    #     pickup_request.fulfilled_by = volunteer
    #     client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    #     message = client.sms.messages.create(to=phone_number, from_="+17202599396", body="Someone has confirmed that they want to pick up your food! %s" % volunteer.id + "-" pickup_request.id)
    # except PickupRequest.DoesNotExist:
    #     return HttpResponse("Pickup request does not exist %s" % request_id)

    return HttpResponse("Fulfill Request Endpoint")

def actions_confirm_request(request,request_id):
    return HttpResponse("Confirm Request Endpoint")

def twilio_callback(request):
    # from_ = request.GET.get("From")
    # body = request.GET.get("Body")
    # body = body.split("-")
    # try
    #     request_user_profile = UserProfile.objects.get(phone_number=from_)
    #     pickup_request = PickupRequest.objects.get(id=body[0])
    #     volunteer = User.objects.get(id=body[1])
    #     pickup_request.is_fulfilled = True
    #     pickup_request.save()
    # except PickupRequest.DoesNotExist:
    #     return HttpResponse("Pickup request does not exist %s" % body)
    # except UserProfile.DoesNotExist:
    #     return HttpResponse("User profile does not exist %s" % from_)
    return HttpResponse("Twilio Callback")

def actions_pickup_request(request,request_id):
    return HttpResponse("Pickup Request Endpoint")

def home(request):
    return render_to_response("home.html",RequestContext(request))

def create_profile(request):
    if request.method == "POST":
        user_profile = UserProfile(
                phone_number=request.POST.get("phone_number"),
                user=request.user,
                donater_description=request.POST.get("donater_description"),
                )
        user_profile.save()
        return redirect("/")
    else:
        """HACK FIXME"""
        user_profile = UserProfile.objects.all();
        return render_to_response("create_profile.html",{'all_requests':all_requests},RequestContext(request))


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

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from twilio.rest import TwilioRestClient
from django.conf import settings
from main.models import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout as auth_logout

@login_required
def logout(request):
    auth_logout(request)
    return redirect("/")

@login_required
def create_pickup_request(request):
    if request.method != "POST":
        raise Http404

    new_request = PickupRequest(
        description = request.POST.get("description",""),
        latitude=request.POST.get("latitude",0),
        longitude=request.POST.get("longitude",0),
        requester=request.user
    )
    new_request.save()
    return HttpResponse("OK")

@login_required
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

@login_required
def actions_confirm_request(request,request_id):
    return HttpResponse("Confirm Request Endpoint")

@login_required
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

@login_required
def actions_pickup_request(request,request_id):
    return HttpResponse("Pickup Request Endpoint")

@login_required
def home(request):
    return render_to_response("home.html",RequestContext(request))

@login_required
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

@login_required
def donation_map(request):
	return render_to_response("donation_map.html",RequestContext(request))

@login_required
def requests(request):
	return render_to_response("requests.html",RequestContext(request))

@login_required
def get_pic_url(request):
    picurl = "https://graph.facebook.com/%s/picture" % request.user.username
    return render_to_response("person.html", {'picurl':picurl})

@login_required
def msg_confirmation(request):
	return render_to_response("msg_confirmation.html",RequestContext(request))

@login_required
def direction_map(request):
    return render_to_response("direction_map.html",RequestContext(request))

@login_required
def feedback(request):
    return render_to_response("feedback.html",RequestContext(request))

@login_required
def picked_up(request):
    return render_to_response("picked_up.html",RequestContext(request))

def sign_in(request):
    return render_to_response("sign_in.html",RequestContext(request))

@login_required
def new_donation(request):
    return render_to_response("new_donation",RequestContext(request))

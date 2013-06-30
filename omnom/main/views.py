from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from twilio.rest import TwilioRestClient
from django.conf import settings
from main.models import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from main.utils import register_required

def logout(request):
    auth_logout(request)
    return redirect("/")

@login_required
@register_required
def create_pickup_request(request):
    if request.method != "POST":
        all_requests = PickupRequest.objects.all()
        return render_to_response("create_request.html", {"all_requests": all_requests},RequestContext(request))

    new_request = PickupRequest(
        description = request.POST.get("description",""),
        latitude=request.POST.get("latitude",0),
        longitude=request.POST.get("longitude",0),
        requester=request.user
    )
    new_request.save()
    return redirect("/create_pickup_request")


@login_required
@register_required
def actions_fulfill_request(request,request_id):
    try:
        pickup_request = PickupRequest.objects.get(id=request_id)
        donnor_phone_number = UserProfile.objects.get(id=pickup_request.requester.id).phone_number
        volunteer = request.user
        client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.sms.messages.create(to=donnor_phone_number, from_="+17202599396", body="Someone has confirmed that they want to pick up your food! Please reply with %s-%s" % (volunteer.id,pickup_request.id))
    except PickupRequest.DoesNotExist:
        return HttpResponse("Pickup request does not exist %s" % request_id)

    return redirect(reverse('direction_map'))


@login_required
@register_required
def actions_confirm_request(request,request_id):
    return HttpResponse("Confirm Request Endpoint")

def twilio_callback(request):
    from_ = request.GET.get("From")
    body = request.GET.get("Body")
    body = body.split("-")
    print body
    try:
        request_user_profile = UserProfile.objects.get(phone_number=from_)
        volunteer = User.objects.get(id=body[0])
        pickup_request = PickupRequest.objects.get(id=body[1])
        pickup_request.is_fulfilled = True
        pickup_request.fulfilled_by = volunteer
        pickup_request.save()
        volunteer_phone_number = UserProfile.objects.get(user_id=volunteer.id).phone_number

        client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.sms.messages.create(to=volunteer_phone_number, from_="+17202599396", body="Donor has already confirmed that you can pick up the food! Come and Grab it, bro!")
    except PickupRequest.DoesNotExist:
        return HttpResponse("Pickup request does not exist %s" % body)
    except UserProfile.DoesNotExist:
        return HttpResponse("User profile does not exist %s" % from_)
    return HttpResponse("Twilio Callback")


@login_required
@register_required
def actions_pickup_request(request,request_id):
    return HttpResponse("Pickup Request Endpoint")


@login_required
@register_required
def home(request):
    return render_to_response("home.html",RequestContext(request))

@login_required
def create_profile(request):
    user_profile = request.user.get_profile()
    if request.method == "POST":
        user_profile.phone_number = request.POST.get("phone_number")
        user_profile.donater_description = request.POST.get("donater_description")
        user_profile.save()
        return redirect("/")
    else:
        return render_to_response("create_profile.html",{'user_profile':user_profile},RequestContext(request))

@login_required
def donation_map(request):
    all_requests = PickupRequest.objects.filter(fulfilled_by__isnull=True)
    return render_to_response("donation_map.html", {"all_requests": all_requests},RequestContext(request))


@login_required
@register_required
def requests(request):
	return render_to_response("requests.html",RequestContext(request))

@login_required
def get_pic_url(request):
    picurl = "https://graph.facebook.com/%s/picture" % request.user.username
    return render_to_response("person.html", {'picurl':picurl},RequestContext(request))

@login_required
def msg_confirmation(request, request_id):
	return render_to_response("msg_confirmation.html", {'request_id': request_id},RequestContext(request))

@login_required
def direction_map(request):
    return render_to_response("direction_map.html",RequestContext(request))

@login_required
def feedback(request):
    return render_to_response("feedback.html",RequestContext(request))

@login_required
def picked_up(request):
    return render_to_response("picked_up.html",RequestContext(request))

@login_required
def my_profile(request):
    picurl = "https://graph.facebook.com/%s/picture?type=large" % request.user.username
    return render_to_response("my_profile.html", {'picurl':picurl},RequestContext(request))

def confirm_pick_up(request):
    return render_to_response("confirm_pick_up.html", RequestContext(request))

def sign_in(request):
    return render_to_response("sign_in.html",RequestContext(request))

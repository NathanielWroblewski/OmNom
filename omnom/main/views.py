from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from twilio.rest import TwilioRestClient
from twilio import TwilioException
from django.conf import settings
from main.models import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from main.utils import register_required
from main.constants import CONFIRMATION_TEXT

def logout(request):
    auth_logout(request)
    return redirect("/")

def splash(request):
    return render_to_response("splash.html",{},RequestContext(request))

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
    if request.method != "POST":
        raise Http404

    try:
        pickup_request = PickupRequest.objects.get(id=request_id)
        donnor_phone_number = UserProfile.objects.get(id=pickup_request.requester.id).phone_number
        volunteer = request.user

        client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID,
                                  settings.TWILIO_AUTH_TOKEN)
        message = client.sms.messages.create(
            to=donnor_phone_number,
            from_="+17202599396",
            body=CONFIRMATION_TEXT % (request.POST.get("minutes",10),
                                      volunteer.id,
                                      pickup_request.id))

    except PickupRequest.DoesNotExist:
        return HttpResponse("Pickup request does not exist %s" % request_id)
    except UserProfile.DoesNotExist:
        return HttpResponse("User Profile not found")

    return redirect(reverse('thank_you'))


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
    pickup_request = get_object_or_404(PickupRequest,pk=request_id)
    return render_to_response("msg_confirmation.html",
                              {'pickup_request': pickup_request},
                              RequestContext(request))

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
    user = request.user
    user_profile = UserProfile.objects.get(user_id=user.id)
    open_donations = PickupRequest.objects.filter(requester=user, fulfilled_by__isnull=True)
    closed_donations = PickupRequest.objects.filter(requester=user, fulfilled_by__isnull=False)
    picurl = "https://graph.facebook.com/%s/picture?type=large" % request.user.username
    return render_to_response("my_profile.html",{'picurl':picurl, "user": user, "user_profile": user_profile, "open_donations": open_donations, "closed_donations": closed_donations},RequestContext(request))

def confirm_pick_up(request):
    return render_to_response("confirm_pick_up.html", RequestContext(request))

def sign_in(request):
    return render_to_response("sign_in.html",RequestContext(request))

def thank_you(request):
    return render_to_response("thank_you.html", RequestContext(request))

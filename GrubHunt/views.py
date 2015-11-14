from django.shortcuts import render
from django.http import HttpResponse
from GrubHunt.models import FoodVendor, UserProfile
from GrubHunt.populate import DatabasePopulater
from GrubHunt.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
import googlemaps
from datetime import datetime


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    context_dict = {}

    # Render the response and send it back!
    return render(request, 'GrubHunt/index.html', context_dict)

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'GrubHunt/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/GrubHunt/list_vendors')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your GrubHunt account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'GrubHunt/login.html', {})
        
# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/GrubHunt/')



@staff_member_required
def update(request):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    added_vendors = DatabasePopulater().populate()
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    #food_vendors = FoodVendor.objects.order_by('-key')[:50]
    #context_dict['food_vendors'] = food_vendors
    context_dict['added_vendors'] = added_vendors

    # Render the response and send it back!
    return render(request, 'GrubHunt/update.html', context_dict)

def vendors(request):
    vendor_list = FoodVendor.objects.order_by('key')
    context_dict = {'vendor_list':vendor_list}
		
    return render(request, 'GrubHunt/vendors.html', context_dict)


def find_route(request,vendor_slug):
    context_dict = {}
	
    try:
		# if we ccannot find a slug with given key raise a exception
        vendor = FoodVendor.objects.get(slug=vendor_slug)
        context_dict['vendor'] = vendor
        context_dict['vendor_slug']=vendor.slug
    except Vendor.DoesNotExist:
        pass
	
    return render (request, 'GrubHunt/find_route.html', context_dict)


def list_vendors(request):

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        vendor_list = FoodVendor.objects.filter(description__contains=q) 
    else:
        vendor_list = FoodVendor.objects.order_by('businessName')

    context_dict = {'vendor_list':vendor_list}

    return render(request, 'GrubHunt/list_vendors.html', context_dict)


def profile(request,userprofile_slug):

    context_dict = {}
    userprofile = UserProfile.objects.get(slug=userprofile_slug)
	# retrieve all vendors associated to the userprofile
    vendors = FoodVendor.objects.filter(userprofile=userprofile)
    
    context_dict['userprofile'] = userprofile
    context_dict['userprofile_slug'] = userprofile.slug
    context_dict['user'] = userprofile.user
    context_dict['vendors'] = vendors
    return render(request, 'GrubHunt/profile.html', context_dict)


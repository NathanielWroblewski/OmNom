from django.contrib.auth.decorators import user_passes_test 

def register_required(function=None, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
            lambda u: u.get_profile().phone_number!="", 
        login_url="my_profile",
        #redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

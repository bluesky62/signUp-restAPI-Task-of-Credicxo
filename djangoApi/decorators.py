from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(viewFunction):
    def wrapperFuc(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog-home')
        else:
            return viewFunction(request, *args, **kwargs)

    return wrapperFuc


def allowed_user(allowed_roles=[]):
    def decorator(viewFunction):
        def wrapperFuc(request, *args, **kwargs):
            group = None
            user = request.user
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return viewFunction(request, *args, **kwargs)
            elif user in redirect.objects.all():
                messages.success(request,
                                 f'your account has been created for {user}. Follow the verifications process.')
                return redirect('logout')
            elif user == AnonymousUser():
                return redirect('login')
            else:
                print(type(user))
                print(user)
                return HttpResponse("You are not authorised to enter the platform")
            return wrapperFuc()

        return decorator()

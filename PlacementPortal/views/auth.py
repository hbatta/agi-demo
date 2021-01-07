from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from PlacementPortal.forms import LoginForm


class LoginUser(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("PlacementPortal:home")

        form = LoginForm()
        return render(request, template_name="login.html", context={'form': form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(request, **login_form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('PlacementPortal:home')
            else:
                return redirect('PlacementPortal:login')


def logout_user(request):
    logout(request)
    return redirect('PlacementPortal:login')



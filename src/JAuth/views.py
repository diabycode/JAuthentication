from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def home(request):
    """ Home page view """

    return render(request, "JAuth/home.html", {})

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, get_user_model


User = get_user_model()

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username") or None
        password = request.POST.get("password") or None
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    return render(request, "accounts/login.html")


def register_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None
        # user_exists_qs = User.objects.filter(username__iexact=username).exists()
        # email_exists_qs = User.objects.filter(email__iexact=username).exists()
        try:
            User.objects.create_user(username, email=email, password=password)
        except:
            pass
    return render(request, "accounts/register.html")
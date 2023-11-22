from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required

from A1_perfiles.forms import UserRegisterForm, UserUpdateForm


def signup_view(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse("login")
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name="signup.html",
        context={"form": formulario},
    )


def login_view(request):
    next_url = request.GET.get("next")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get("username")
            password = data.get("password")
            user = authenticate(username=usuario, password=password)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse("home")
                return redirect(url_exitosa)
    else:
        form = AuthenticationForm()
    return render(
        request=request,
        template_name="login.html",
        context={"form": form},
    )


class logout_view(LogoutView):
    success_url = reverse_lazy("home")


class edit_view(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy("home")
    template_name = "edit_profile.html"

    def get_object(self, queryset=None):
        return self.request.user


def profile_view(request):
    user = request.user
    contexto = {
        "usuario": user,
    }
    return render(request, "profile.html", context=contexto)


def profile_delete_view(request):
    user = request.user
    if request.method == "POST":
        user.delete()
        url_exitosa = reverse("home")
        return redirect(url_exitosa)

    return render(request, "delete_profile.html")

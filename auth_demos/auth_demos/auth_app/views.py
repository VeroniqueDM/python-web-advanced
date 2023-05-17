from django import forms
from django.contrib.auth import login, forms as auth_forms, get_user_model, views as auth_views, mixins as auth_mixins
from django.contrib.auth.views import LoginView

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# def my_view(request):
#     user = None
#     login(request, user)
from auth_demos.auth_app.models import Profile

UserModel = get_user_model()


class RestrictedView(auth_mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'



class UserRegistrationForm(auth_forms.UserCreationForm):
    # Takes everything that UserCreationForm already has because of inheritance

    # class Meta:
    #     model = UserModel
    #     fields = ('username', 'first_name')
    #

    first_name = forms.CharField(
        max_length=25,
    )

    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            **self.cleaned_data,
            # first_name=self.cleaned_data['first_name'],
            user=user,
        )
        if commit:
            profile.save()

        return user

# To add additional info given in Profile model by registration.
# class ProfileCreateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ('user', )

class UserRegistrationView(generic.CreateView):
    # Built-in functionality
    # form_class = forms.UserCreationForm

    # With custom form_class
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        # user => self.objects
        # request => self.request

        login(self.request, self.object)
        return result


# def login_user(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = UserModel.objects.get(username=username)
#     login(request, user)

class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    template_name = 'logout.html'
    # success_url_allowed_hosts =
    # def get_success_url(self):
    #     return reverse_lazy('index')


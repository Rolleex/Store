from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from .serializers import UserRegisterSerializers, ProfileRegisterSerializer, ProfileSerializer


# Create your views here.
def register_user(request):
    """ Register User and Profile model"""

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()

            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('home')
    else:
        form = RegisterForm()
        profile_form = ProfileForm()
    return render(request, 'user_profile/register.html', {'form': form, 'profile_form': profile_form})


class RegisterAPIView(APIView):
    """ API View for Register User and Profile"""

    def post(self, request):
        user_serialize = UserRegisterSerializers(data=request.data)
        profile_serialize = ProfileRegisterSerializer(data=request.data)
        if user_serialize.is_valid(raise_exception=True) and profile_serialize.is_valid(raise_exception=True):
            user_new = user_serialize.save()
            profile_new = profile_serialize.save(user=user_new)
            return Response(user_serialize.data, status=status.HTTP_201_CREATED)
        return Response(user_serialize.data, status=status.HTTP_400_BAD_REQUEST)


def login_user(request):
    """ Check valid form and login user"""
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'user_profile/login.html', {'form': form})


def logout_user(request):
    """default logout func"""
    logout(request)
    return redirect('login')


class ProfilePage(DetailView):
    """ Detail profile page """
    model = Profile
    template_name = 'user_profile/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        """" For auth users """
        return get_object_or_404(self.model, user=self.request.user)

    def get_context_data(self, **kwargs):
        """" for orders list """
        pass


class ProfilePageApiView(APIView):
    """API Profile page detail"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """" Get auth user profile """
        profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        """"" Update profile """
        profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
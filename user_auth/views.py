from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes,permission_classes
from rest_framework import status
from user_auth.serializers import UserRegisterSerializer
from rest_framework.renderers import HTMLFormRenderer
from user_auth.forms import UserRegisterForm
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def user_register_page(request):
    if request.method == 'GET':
        form = UserRegisterForm()
        #return render(request,'user_auth/register.html',
                #{'form': form,'registered':registered})
        return render(request,'user_auth/register.html',{'form':form})

    #if request.method == 'POST':
        #print request.META['HTTP_ACCEPT']
        #if request.META['HTTP_ACCEPT'].split(',')[0].find('html')>0:
            #register = UserRegisterForm(request.DATA)
            #if register.is_valid():
                #user=register.save()
                #user.set_password(user.password)
                #user.save()
                #return render(request,'user_auth/register_ok.html')
            #return render(request,'user_auth/register.html',{'form':register})

@api_view(['POST'])
#@permission_classes((IsAuthenticated,))
def user_register(request):
        register = UserRegisterSerializer(data=request.DATA)
        if register.is_valid():
            user=register.save()
            user.set_password(user.password)
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(register.errors,status=status.HTTP_400_BAD_REQUEST) 

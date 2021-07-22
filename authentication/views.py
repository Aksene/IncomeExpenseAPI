from inspect import currentframe
from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerialezer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import EmailMessage


# Create your views here. 
# AKA Endpoints

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerialezer

    # Make a post request to the API
    def post(self,request):
        user = request.data
        # Pass,validate then save the data
        serializers = self.serializer_class(data=user)
        serializers.is_valid(raise_exception=True)
        serializers.save

        # Returns the User data
        user_data = serializers.data
        #user = User.objects.get(email=user_data['email'])
        #user = User.objects.filter(email=user_data['email'])

        token = RefreshToken.for_user(User).access_token

        # Get the current site 
        current_site = get_current_site(request).domain
        # Get url police file (takes the URL name then returns the path) 
        relativeLink= reverse('email-verify')
       
        absurl= 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Dear '+user_data.get('username') +',\n Use link below to verify your email \n'+ absurl +"\nIf clicking the link above doesn't work, please copy and paste the URL in a new browser window instead. \n" +'\nSincerly, \n' +'Distaff Team \n'
        #Static method
        #Util.send_email(data)

        try:
            data={ 'email_subject': 'Distaff Verification Mail', 'email_body': email_body, 'to_email': user_data.get('email')}
            email = EmailMessage(
                subject=data['email_subject'], body=data['email_body'],to=[data['to_email']])
            response = email.send()
        except Exception as e:
                    pass
        


        #### THIS IS THE OG SERVER METHOD ####
        # try:
        #             subject = "Verification Mail"

        #             email_body = """\
        #                 <html>
        #                     <head></head>
        #                     <body>
        #                         <h2>Dear %s, </h2>
        #                         <p> To initiate the verification process,
        #                          Please click the link below:</p>
        #                         <p> %s </p>
        #                         <p>If clicking the link above doesn't work, please copy and paste the URL in a new browser
        #                         window instead.</p>
        #                         <p>Sincerely, </p>
        #                         <p>Distaff Team 
        #                         </p>
        #                     </body>
        #                 </html>
        #                 """ %(user_data.get('username'), absurl)
        #             email = EmailMessage('Email Verification Mail! ', email_body, to=user_data.get('email'))
        #             email.content_subtype = "html"
        #             email.send()
        # except Exception as e:
        #             pass


        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass
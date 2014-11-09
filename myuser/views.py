from httplib import HTTPResponse
import json
from django.db.models import F
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from django.utils import timezone
from myuser.models import MyUser
from myuser.serializer.myuser_serializer import MyUserSerializer



__author__ = 'challa'
from rest_framework import generics, permissions


class CreateMyUserView(generics.ListCreateAPIView):
    model = MyUser
    serializer_class = MyUserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        req_data = request.DATA
        if username_exists(req_data['username']):
            return Response('Username already exists', status=status.HTTP_400_BAD_REQUEST)

        serialized = MyUserSerializer(data=req_data)
        if serialized.is_valid():
            try:
                created_user = MyUser.objects.create_user(**req_data)
                return Response(MyUserSerializer(instance=created_user, context={'request': request}).data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                raise( 400, e.message)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class MyUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = MyUser
    serializer_class = MyUserSerializer
    permission_classes = (permissions.AllowAny,)
    def update(self, request, *args, **kwargs):
        req_data = request.DATA
        req_data['modified_date'] = timezone.now()
        qs = MyUser.objects.get(id=int(kwargs['pk']))
        serializer = MyUserSerializer(qs, data=req_data, partial=True)

        if serializer.is_valid():
            self.object = serializer.save(force_update=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckUserAvailabiltyView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.DATA['username']
        response_data = {}
        response_data['result'] = username_exists(username)
        return Response(json.dumps(response_data), content_type="application/json", status=status.HTTP_200_OK)

def username_exists(username):
    if MyUser.objects.filter(username=username).exists():
            return True
    else:
            return False
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .models import Contact
from .serializers import UserRegSerializer, ContactSerializer


def profileView(request):
    '''вьюха для приветствия при регистрации'''
    template = 'accounts/index.html'
    context = {'user': request.user}
    return render(request, template, context)


# https://www.youtube.com/watch?v=ddB83a4jKSY&t=1829s
@permission_classes([IsAuthenticated,])
class RestrictedApiView(APIView):
    '''пример для отображения данных в зависимости от типа пользователя'''
    def get(self, request, *args, **kwargs):
        if request.user.type == 'buyer':
            data = f'{request.user}, Вы покупатель'
        elif request.user.type == 'shop':
            data = f'{request.user}, Вы продавец'
        return Response(data)


#https://www.youtube.com/watch?v=_OhF6FEdIao&list=PLgCYzUzKIBE9Pi8wtx8g55fExDAPXBsbV&index=6
# 11:10
class RegistrationView(APIView):
    def post(self, request):
        serializer = UserRegSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully created a new User'
            data['user'] = user.email
        else:
            data = serializer.errors
        return Response(data)


class ContactView(APIView):
    def get(self, request):
        contacts = request.user.contacts.first()
        serializer = ContactSerializer(contacts)
        return Response(serializer.data)

    def put(self, request):
        contacts = request.user.contacts.first()
        serializer = ContactSerializer(contacts, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = f'Successfully updated user ({request.user}) contacts'
            data['type'] = request.user.type
            data['data'] = serializer.data
        else:
            raise serializer.errors
        return Response(data)

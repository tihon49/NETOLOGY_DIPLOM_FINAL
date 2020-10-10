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


@permission_classes([IsAuthenticated])
class ContactView(APIView):
    def get(self, request):
        try:
            contact = Contact.objects.get(user=request.user)
            serializer = ContactSerializer(contact)
        except:
            return Response({'response': f'{request.user} has no contacts. You can make PUT request'})
        return Response(serializer.data)

    def put(self, request):
        contact, _ = Contact.objects.get_or_create(user=request.user)
        serializer = ContactSerializer(contact, request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            raise serializer.errors
        return Response(serializer.data)

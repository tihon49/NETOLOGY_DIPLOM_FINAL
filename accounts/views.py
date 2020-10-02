from pprint import pprint

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


def profileView(request):
    template = 'accounts/index.html'
    context = {'user': request.user}
    return render(request, template, context)


# https://www.youtube.com/watch?v=ddB83a4jKSY&t=1829s
@permission_classes([IsAuthenticated])
class RestrictedApiView(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.type == 'buyer':
            data = f'{request.user}, Вы покупатель'
        elif request.user.type == 'shop':
            data = f'{request.user}, Вы продавец'
        return Response(data=data, status=status.HTTP_200_OK)
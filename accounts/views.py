from django.shortcuts import render


def profileView(request):
    template = 'accounts/index.html'
    context = {'user': request.user}
    return render(request, template, context)
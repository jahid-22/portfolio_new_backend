from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
import os

from .serializers import ServicesSerializer , PortfolioSerializer
from .models import Services, Category, Portfolio

# Service section 
@api_view(['GET'])
def services(request):
    service = Services.objects.all().order_by('-id')
    serializers  = ServicesSerializer(service, many=True)  
    return Response(serializers.data, status= 201)

# Portfolio section. Fetching all data
@api_view(['GET'])
def portfolio(request):
    portfolio_all = Portfolio.objects.all().order_by('-id')
    serializer_all = PortfolioSerializer(portfolio_all, many=True)
    return Response({
        'portfolio_all': serializer_all.data })

# Portfolio section. Fetching Designed data
@api_view(['GET'])
def portfolioDesign(request):
    portfolio_design = Portfolio.objects.filter(category__slug='designed')
    serializer_design = PortfolioSerializer(portfolio_design, many=True)
    return Response({'portfolio_design': serializer_design.data })


# Portfolio section. Fetching Developed data
# @api_view(['GET'])
# def portfolioDevelop(request):
#     portfolio_developed = Portfolio.objects.filter(category__slug='developed')
#     serializer_developed = PortfolioSerializer(portfolio_design, many=True)
#     return Response({'portfolio_developed': serializer_developed.data})

# Portfolio section. Fullstack  data
# @api_view(['GET'])
# def portfolioFull(request):
#     portfolio_fullstack = Portfolio.objects.filter(category__slug='	fullstack')
#     serializer_fullstack = PortfolioSerializer(portfolio_design, many=True)
#     return Response({
#         'portfolio_fullstack': serializer_fullstack.data
#     })



# Form submission
@api_view(['POST'])
def contact_form(request):
    if request.method == 'POST':
        name = request.data.get('username')
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')
    
        send_mail(
        subject = subject,
        message = message,
        from_email = email,
        recipient_list = [os.environ.get('EMAIL_HOST_USER')],
        fail_silently = False,
        )
    return  Response({"msg":"success, Email !!"})
    
    

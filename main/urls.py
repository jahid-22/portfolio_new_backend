from . import views
from django.urls import path



urlpatterns = [
    path('form/', views.contact_form, name="contact_form"),
    path('services/', views.services, name ="services"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolioDesign/', views.portfolioDesign, name="portfolioDesign"),
    # path('portfolioDevelop/', views.portfolioDevelop, name="portfolioDevelop"),
    # path('portfolioFull/', views.portfolio, name="portfolioFull"),
]

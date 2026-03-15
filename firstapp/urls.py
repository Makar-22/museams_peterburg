from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('catalog',views.catalog),
    path('cuntscamera',views.cuntscamera),
    path('ermitaj',views.ermitaj),
    path('faberje',views.faberje),
    path('rusmuz',views.rusmuz),
    path('peter',views.peter),
    path('era',views.era),
    path('fortress',views.fortress),
    path('pushkin',views.pushkin),
    path('mramor',views.mramor),
    path('zapovednik',views.zapovednik
    ),
]

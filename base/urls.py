"""
apppppppppppppppppppppppppppppppppppppppppp
"""
from django.contrib import admin
from django.urls import path
from django.views import View
from rest_framework_simplejwt.views import TokenObtainPairView

from base import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('secret', views.secret),
    path('books/<int:id>', views.books),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]

"""
URL configuration for spanish_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_and_moderation/', include("admin_and_moderation.urls")),
    path('analytics', include("analytics.urls")),
    path('content_delivery_network', include("content_delivery_network.urls")),
    path('content_management', include("content_management.urls")),
    path('exercise_and_quiz', include("exercise_and_quiz.urls")),
    path('feedback_and_support', include("feedback_and_support.urls")),
    path('gamification', include("gamification.urls")),
    path('internationalization', include("internationalization.urls")),
    path('notification_and_messaging', include("notification_and_messaging.urls")),
    path('payment_and_billing', include("payment_and_billing.urls")),
    path('progress_tracking', include("progress_tracking.urls")),
    path('search_and_recommendation', include("search_and_recommendation.urls")),
    path('user_management', include("user_management.urls")),
]

"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import views as api_views

urlpatterns = [
    # Main Page
    path("", api_views.Main.as_view(), name="api-main"),
    # Compile API, receive source code and push compile task to background queue (async)
    path("compile", api_views.Compile.as_view(), name="api-compile"),
    # Compile Result Check API from unique source code ID
    path("result/<int:id>", api_views.CompileResult.as_view(), name="api-result"),
]

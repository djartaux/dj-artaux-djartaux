from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

from authentication.models import User


@login_required
def home(request):
    """
    Description: vue pour la page accueil.
    Paramètre(s):
    - request: le paramètre par défaut indispensable
    """
    return render(request, "topblog/home.html")

def coucou(request):
    return render(request, "topblog/coucou.html")

import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

from housing_backend import admin, models

# Basic scaffolding for testing custom django admin classes and functions

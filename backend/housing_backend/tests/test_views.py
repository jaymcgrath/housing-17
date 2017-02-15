import pytest

from django.test import RequestFactory
from django.urls import reverse

from housing_backend.views import AffordableList, AffordableFilter, AffordableDetail

pytestmark = pytest.mark.django_db

from mixer.backend.django import mixer
from housing_backend.models import Affordable
from django.db import models


class TestAffordableListView:
    def test_anonymous_access(self):
        url = reverse('affordable_list')
        req = RequestFactory().get(url)
        resp = AffordableList.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"
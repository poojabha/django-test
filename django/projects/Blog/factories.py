import factory
from faker import Factory
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import Blogapp.models
User = get_user_model()
faker = Factory.create()
class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        for i in range(10):
            name = faker.name()
            email = ".".join(name.lower().split()) + "@xyz"
            is_Admin = True
            password = 123;
            user = User.objects.create(username=name, email=email, password=password, is_Admin=is_Admin)
            user.save()
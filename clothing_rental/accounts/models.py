from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from products.models import ClothingItem


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, first_name, last_name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)


    # without those two you won't be able to log into django-admin
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    # comes from PermissionMixin
    is_superuser = models.BooleanField(default=False)

    # every model has to have the manager
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clothing_items = models.ManyToManyField(ClothingItem, null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_shopping_cart(sender, instance, created, **kwargs):
        if created:
            ShoppingCart.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_shopping_cart(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f" {self.user}'s cart{self.id}"

class Favourite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clothing_items = models.ManyToManyField(ClothingItem, null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_favorite(sender, instance, created, **kwargs):
        if created:
            Favourite.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_favorite(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f" {self.user} likes {self.clothing_items}"


"""END OF NEW """


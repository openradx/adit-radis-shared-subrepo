"""
Django settings for example_project project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

import environ
import toml

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DJANGO_ALLOWED_HOSTS=(list, ["localhost"]),
    DJANGO_CSRF_TRUSTED_ORIGINS=(list, []),
    SITE_DOMAIN=(str, "localhost"),
    DJANGO_INTERNAL_IPS=(list, ["127.0.0.1"]),
    FORCE_DEBUG_TOOLBAR=(bool, False),
    USER_TIME_ZONE=(str, "Europe/Berlin"),
    SERVER_EMAIL=(str, "adit.support@example.org"),
    SUPPORT_EMAIL=(str, "adit.support@example.org"),
    TOKEN_AUTHENTICATION_SALT=(str, "Rn4YNfgAar5dYbPu"),
)

# Take environment variables from .env file
env.read_env(BASE_DIR / ".." / ".env")

# Read pyproject.toml to fetch current version. We do this conditionally as the
# ADIT client library uses ADIT for integration tests installed as a package
# (where no pyproject.toml is available).
if (BASE_DIR / ".." / "pyproject.toml").exists():
    pyproject = toml.load(BASE_DIR / ".." / "pyproject.toml")
    PROJECT_VERSION = pyproject["tool"]["poetry"]["version"]
else:
    PROJECT_VERSION = "???"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4q3@c!62pzy74p2dck1^=d3dyl_gc#zk1bewa@8ch3(czs3bir"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS")

CSRF_TRUSTED_ORIGINS = env("DJANGO_CSRF_TRUSTED_ORIGINS")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Used by the django.contrib.sites framework
SITE_ID = 1

SITE_DOMAIN = env("SITE_DOMAIN")
SITE_NAME = "Example Project"
SITE_META_KEYWORDS = "ADIT,RADIS"
SITE_META_DESCRIPTION = "Shared apps between ADIT and RADIS"
SITE_PROJECT_URL = "https://github.com/openradx/adit-radis-shared"

# Application definition

INSTALLED_APPS = [
    "daphne",
    "adit_radis_shared.common.apps.CommonConfig",  # must be before "registration"
    "registration",  # should be immediately above "django.contrib.admin"
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
    "django_extensions",
    "loginas",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_htmx",
    "django_tables2",
    "rest_framework",
    "adit_radis_shared.accounts.apps.AccountsConfig",
    "adit_radis_shared.token_authentication.apps.TokenAuthenticationConfig",
    "example_project.example_app.apps.ExampleAppConfig",
    "debug_toolbar",
    "debug_permissions",
    "django_browser_reload",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "adit_radis_shared.accounts.middlewares.ActiveGroupMiddleware",
    "adit_radis_shared.common.middlewares.MaintenanceMiddleware",
    "adit_radis_shared.common.middlewares.TimezoneMiddleware",
]

ROOT_URLCONF = "example_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "adit_radis_shared.common.site.base_context_processor",
            ],
        },
    },
]

WSGI_APPLICATION = "example_project.wsgi.application"

ASGI_APPLICATION = "example_project.asgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Custom user model
AUTH_USER_MODEL = "accounts.User"

# A custom authentication backend that supports a single currently active group.
AUTHENTICATION_BACKENDS = ["adit_radis_shared.accounts.backends.ActiveGroupModelBackend"]

# All REST API requests must come from authenticated clients
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "adit_radis_shared.token_authentication.auth.RestTokenAuthentication",
    ],
}

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# This seems to be important for development on Gitpod as CookieStorage
# and FallbackStorage does not work there.
# Seems to be the same problem with Cloud9 https://stackoverflow.com/a/34828308/166229
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INTERNAL_IPS = env("DJANGO_INTERNAL_IPS")

if env("FORCE_DEBUG_TOOLBAR"):
    # https://github.com/jazzband/django-debug-toolbar/issues/1035
    from django.conf import settings

    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: settings.DEBUG}

# A timezone that is used for users of the web interface.
USER_TIME_ZONE = env("USER_TIME_ZONE")

# For crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# django-templates2
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap5.html"

# An Email address used by the ADIT server to notify about finished jobs and
# management notifications.
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL")
DEFAULT_FROM_EMAIL = SERVER_EMAIL

# A support Email address that is presented to the users where
# they can get support.
SUPPORT_EMAIL = env("SUPPORT_EMAIL")

# The salt that is used for hashing new tokens in the token authentication app.
# Cave, changing the salt after some tokens were already generated makes them all invalid!
TOKEN_AUTHENTICATION_SALT = env("TOKEN_AUTHENTICATION_SALT")

# We need to define a dummy host and port for the Flower server as we setup a reverse proxy
# to access Flower in ADIT and RADIS behind the Django authentication. But we don't use
# Flower in our example project (as we don't have the Celery stuff in it).
FLOWER_HOST = "localhost"
FLOWER_PORT = 5555

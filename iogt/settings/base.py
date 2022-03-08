"""
Django settings for iogt project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import allauth
from django.contrib import auth
from django.utils.translation import gettext_lazy as _

import django.conf.locale

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'home',
    'search',
    'iogt_users',
    'comments',
    'iogt_content_migration',
    'questionnaires',
    'messaging',
    'common',
    'django.contrib.humanize',
    'wagtail_localize',
    'wagtail_localize.locales',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.modeladmin',
    'wagtailmenus',
    'wagtailmedia',
    'wagtailmarkdown',
    'wagtail_transfer',
    'wagtailsvg',
    'wagtail.contrib.settings',

    'django_comments_xtd',
    'django_comments',
    'modelcluster',
    'taggit',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'sass_processor',
    'translation_manager',
    'health_check',
    'health_check.db',
    'health_check.cache',
    'health_check.storage',
    'health_check.contrib.migrations',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'iogt.middleware.GlobalContextMiddleware',
    "iogt.middleware.LocaleMiddleware",
    "iogt.middleware.AdminLocaleMiddleware",
    'iogt.middleware.CustomRedirectMiddleware',
    'iogt_users.middlewares.RegistrationSurveyRedirectMiddleware',
    'external_links.middleware.RewriteExternalLinksMiddleware',
    'iogt.middleware.CacheControlMiddleware',
]

# Prevent Wagtail's built in menu from showing in Admin > Settings
WAGTAILMENUS_MAIN_MENUS_EDITABLE_IN_WAGTAILADMIN = False

ROOT_URLCONF = 'iogt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "wagtail.contrib.settings.context_processors.settings",
                'wagtailmenus.context_processors.wagtailmenus',
                'wagtail.contrib.settings.context_processors.settings',
                "home.processors.show_welcome_banner",
                'django.template.context_processors.i18n',
                'home.processors.commit_hash',
                'home.processors.show_footers',
            ],
        },
    },
]

WSGI_APPLICATION = 'iogt.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Authentication
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

AUTH_USER_MODEL = 'iogt_users.User'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 4
        }
    }
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'static')

# Allauth settings (https://django-allauth.readthedocs.io/en/latest/configuration.html)
# ACCOUNT_SIGNUP_FORM_CLASS = 'iogt_users.forms.AccountSignUpAdditionalFieldsForm'

# Control the forms that django-allauth uses
ACCOUNT_FORMS = {
    "login": "allauth.account.forms.LoginForm",
    "add_email": "allauth.account.forms.AddEmailForm",
    "change_password": "iogt_users.forms.ChangePasswordForm",
    "set_password": "allauth.account.forms.SetPasswordForm",
    "reset_password": "allauth.account.forms.ResetPasswordForm",
    "reset_password_from_key": "allauth.account.forms.ResetPasswordKeyForm",
    "disconnect": "allauth.socialaccount.forms.DisconnectForm",
    # Use our custom signup form
    "signup": "iogt_users.forms.AccountSignupForm",
}
# ACCOUNT_SIGNUP_FORM_CLASS = 'iogt_users.extra_forms.AccountSignUpAdditionalFieldsForm'

# Wagtail settings

WAGTAIL_SITE_NAME = "IoGT"
ACCOUNT_ADAPTER = 'iogt_users.adapters.AccountAdapter'

WAGTAIL_USER_EDIT_FORM = 'iogt_users.forms.WagtailAdminUserEditForm'
WAGTAIL_USER_CREATION_FORM = 'iogt_users.forms.WagtailAdminUserCreateForm'
WAGTAIL_USER_CUSTOM_FIELDS = ['display_name', 'first_name', 'last_name', 'email', 'terms_accepted']

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = os.getenv('BASE_URL')

# SITE ID
SITE_ID = 1

# Comments
COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL = 1

# Miscellaneous
LOGIN_REDIRECT_URL = "user_profile"
ACCOUNT_LOGOUT_REDIRECT_URL = "logout_redirect"
LOGIN_URL = 'account_login'
WAGTAIL_FRONTEND_LOGIN_URL = LOGIN_URL

#  To help obfuscating comments before they are sent for confirmation.
COMMENTS_XTD_SALT = (b"Timendi causa est nescire. "
                     b"Aequam memento rebus in arduis servare mentem.")

# Source mail address used for notifications.
COMMENTS_XTD_FROM_EMAIL = "noreply@example.com"

# Contact mail address to show in messages.
COMMENTS_XTD_CONTACT_EMAIL = "helpdesk@example.com"

COMMENTS_XTD_CONFIRM_EMAIL = False

COMMENTS_XTD_FORM_CLASS = 'comments.forms.CommentForm'



COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'default': {
        'allow_flagging': True,
        'allow_feedback': True,
        'show_feedback': True,
        'who_can_post': 'users'
    }
}

WAGTAIL_I18N_ENABLED = True

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ('ar', _('Arabic')),
    ('ny', _('Chichewa')), # previously 'ch'
    ('en', _('English')),
    ('fr', _('French')),
    ('id', _('Indonesian')),
    ('kaa', _('Karakalpak')),
    ('km', _('Khmer')),
    ('rw', _('Kinyarwanda')),
    ('rn', _('Kirundi')),
    ('ku', _('Kurdish')),
    ('mg', _('Malagasy')),
    ('ne', _('Nepali')),
    ('nr', _('Ndebele')),
    ('pt', _('Portuguese')),
    ('qu', _('Quechua')),
    ('ru', _('Russian')),
    ('sn', _('Shona')), # previously 'sho'
    ('es', _('Spanish')),
    ('sw', _('Swahili')),
    ('tg', _('Tajik')),
    ('ti', _('Tigrinya')),
    ('ur', _('Urdu')),
    ('uz', _('Uzbek')),
    ('zu', _('Zulu')),
    ('xy', _('Testing')),
]

EXTRA_LANG_INFO = {
    'ku': {
        'bidi': False,
        'code': 'ku',
        'name': 'Kurdish',
        'name_local': 'Kurdish'
    },
    'kaa': {
        'bidi': False,
        'code': 'kaa',
        'name': 'Karakalpak',
        'name_local': 'Karakalpak'
    },
    'mg': {
        'bidi': False,
        'code': 'mg',
        'name': 'Malagasy',
        'name_local': 'Malagasy',
    },
    'nr': {
        'bidi': False,
        'code': 'nr',
        'name': 'Ndebele',
        'name_local': 'Ndebele',
    },
    'ny': {
        'bidi': False,
        'code': 'ny',
        'name': 'Chichewa',
        'name_local': 'Chichewa',
    },
    'qu': {
        'bidi': False,
        'code': 'qu',
        'name': 'Quechua',
        'name_local': 'Quechua',
    },
    'rn': {
        'bidi': False,
        'code': 'rn',
        'name': 'Kirundi',
        'name_local': 'Ikirundi',
    },
    'rw': {
        'bidi': False,
        'code': 'rw',
        'name': 'Kinyarwanda',
        'name_local': 'Kinyarwanda',
    },
    'sn': {
        'bidi': False,
        'code': 'sn',
        'name': 'Shona',
        'name_local': 'Shona',
    },
    'ti': {
        'bidi': False,
        'code': 'ti',
        'name': 'Tigrinya',
        'name_local': 'Tigrinya',
    },
    'zu': {
        'bidi': False,
        'code': 'zu',
        'name': 'Zulu',
        'name_local': 'Zulu',
    },
    'xy': {
        'bidi': False,
        'code': 'xy',
        'name': 'Testing',
        'name_local': 'Testing',
    },
}

django.conf.locale.LANG_INFO.update(EXTRA_LANG_INFO)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

TRANSLATIONS_BASE_DIR = BASE_DIR

# ========= Rapid Pro =================
RAPIDPRO_BOT_USER_ID = os.getenv('RAPIDPRO_BOT_USER_ID')
RAPIDPRO_BOT_USER_USERNAME = os.getenv('RAPIDPRO_BOT_USER_USERNAME')
RAPIDPRO_BOT_USER_PASSWORD = os.getenv('RAPIDPRO_BOT_USER_PASSWORD')

# Wagtail transfer default values. Override these in local.py
WAGTAILTRANSFER_SECRET_KEY = os.getenv('WAGTAILTRANSFER_SECRET_KEY')
WAGTAILTRANSFER_SOURCES = {}

WAGTAILMENUS_FLAT_MENU_ITEMS_RELATED_NAME = 'iogt_flat_menu_items'

WAGTAIL_RICH_TEXT_FIELD_FEATURES = [
    'h2', 'h3', 'h4',
    'bold', 'italic',
    'ol', 'ul',
    'hr',
    'link',
    'document-link',
    'image',
]

# Search results
SEARCH_RESULTS_PER_PAGE = 10


COMMIT_HASH = os.getenv('COMMIT_HASH')

from .profanity_settings import *

EXPORT_FILENAME_TIMESTAMP_FORMAT = '%Y-%m-%dT%H%M%S'

WAGTAILMARKDOWN = {
    'allowed_tags': ['i', 'b'],
}

TRANSLATIONS_PROJECT_BASE_DIR = BASE_DIR

from iogt.patch import *

WAGTAILTRANSFER_UPDATE_RELATED_MODELS = ['wagtailimages.image', 'wagtailsvg.svg',]
WAGTAILTRANSFER_SHOW_ERROR_FOR_REFERENCED_PAGES = True

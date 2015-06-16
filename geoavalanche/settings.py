# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
from geonode.settings import *
#
# General Django development settings
#

SITENAME = 'geoavalanche'

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "geoavalanche.wsgi.application"


# Load more settings from a file called local_settings.py if it exists
try:
    from local_settings import *
except ImportError:
    pass

# Set debug configuration
# DEBUG = True

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

# Location of url mappings
ROOT_URLCONF = 'geoavalanche.urls'

# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

INSTALLED_APPS = (
                  'twitter_tag',
                  'django_mailgun',
                 ) + INSTALLED_APPS

# Make sure to replace with your own values, theses are just made up
#
##Twitter timeline projref: https://github.com/coagulant/django-twitter-tag
# Your access token: Access token
TWITTER_OAUTH_TOKEN = ''
# Your access token: Access token secret
TWITTER_OAUTH_SECRET = ''
# OAuth settings: Consumer key
TWITTER_CONSUMER_KEY = ''
# OAuth settings: Consumer secret
TWITTER_CONSUMER_SECRET = ''

GEOAVALANCHE_EMAIL_ADDRESS = 'geoavalanche@icloud.com'

# if DEBUG:
#	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
##Mailgun service configuration projref: https://github.com/BradWhittington/django-mailgun
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = ''
MAILGUN_SERVER_NAME = ''
#
# -*- coding: utf-8 -*-
#
#  This file is part of django-taggit-autocomplete-modified.
#
#  DESCRIPTION_DESCRIPTION_DESCRIPTION
#
#  Development Web Site:
#    - http://www.codetrax.org/projects/django-taggit-autocomplete-modified
#  Public Source Code Repository:
#    - https://source.codetrax.org/hgroot/django-taggit-autocomplete-modified
#
#  Copyright 2011 George Notaras <gnot [at] g-loaded.eu>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from django.conf import settings

# Set the Tag model that should be used.
TAGGIT_AUTOCOMPLETE_TAG_MODEL = getattr(settings, 'TAGGIT_AUTOCOMPLETE_TAG_MODEL', 'taggit.Tag')

# Override TAGGIT_AUTOCOMPLETE_JS_ROOT in settings.py
DEFAULT_TAGGIT_AUTOCOMPLETE_JS_BASE_URL = '%s/taggit_autocomplete_modified' % settings.STATIC_URL.rstrip('/')
TAGGIT_AUTOCOMPLETE_JS_BASE_URL = getattr(settings, 'TAGGIT_AUTOCOMPLETE_JS_BASE_URL', DEFAULT_TAGGIT_AUTOCOMPLETE_JS_BASE_URL)

# Override TAGGIT_AUTOCOMPLETE_CSS_ROOT in settings.py
DEFAULT_TAGGIT_AUTOCOMPLETE_CSS_BASE_URL = '%s/taggit_autocomplete_modified' % settings.STATIC_URL.rstrip('/')
TAGGIT_AUTOCOMPLETE_CSS_BASE_URL = getattr(settings, 'TAGGIT_AUTOCOMPLETE_CSS_BASE_URL', DEFAULT_TAGGIT_AUTOCOMPLETE_CSS_BASE_URL)

# TODO: Add a setting for the autocomplete options: http://docs.jquery.com/Plugins/Autocomplete/autocomplete#url_or_dataoptions

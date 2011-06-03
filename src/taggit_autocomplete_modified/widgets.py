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


from django.forms.widgets import Input
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from taggit_autocomplete_modified import settings


class TagAutocomplete(Input):
    input_type = 'text'
    
    class Media:
        css = {
            'all': ('%s/jquery.autocomplete.css' % settings.TAGGIT_AUTOCOMPLETE_CSS_BASE_URL,)
        }
        js = (
            # The jquery library should be added by your project
            '%s/jquery.autocomplete.js' % settings.TAGGIT_AUTOCOMPLETE_JS_BASE_URL,
        )
    
    def render(self, name, value, attrs=None):
        json_view = reverse('taggit_autocomplete_modified_tag_list')
        html = super(TagAutocomplete, self).render(name, value, attrs)
        js = u'<script type="text/javascript">jQuery().ready(function() { jQuery("#%s").autocomplete("%s", { multiple: true }); });</script>' % (attrs['id'], json_view)
        return mark_safe("\n".join([html, js]))
    


from django.utils.translation import ugettext_lazy as _

from taggit.forms import TagField
from taggit.managers import TaggableManager

from widgets import TagAutocomplete


class TaggableManagerAutocomplete(TaggableManager):
    def formfield(self, form_class=TagField, **kwargs):
        defaults = {
            'label': _('Tags'),
            'help_text': _('Enter a comma-delimited list of tags.'),
            'required': not self.blank,
            'widget': TagAutocomplete,
        }
        defaults.update(kwargs)
        
        return form_class(**defaults)


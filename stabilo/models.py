from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class Category(models.Model):
    label = models.CharField(_('label'), max_length=50)
    slug = models.SlugField(_('slug'), max_length=50)
    
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('label',)
    
    def __str__(self):
        return self.label

@python_2_unicode_compatible
class Keyword(models.Model):
    keyword = models.CharField(_('keyword'), max_length=250)
    category = models.ForeignKey(Category,
                                    verbose_name=_('category'),
                                    related_name='keywords')
    
    class Meta:
        verbose_name = _('keyword')
        verbose_name_plural = _('keywords')
        ordering = ('keyword',)
    
    def __str__(self):
        return self.keyword

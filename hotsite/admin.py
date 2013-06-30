from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.db import models
from pagedown.widgets import AdminPagedownWidget


class NewFlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {models.TextField: {'widget': AdminPagedownWidget}}

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, NewFlatPageAdmin)

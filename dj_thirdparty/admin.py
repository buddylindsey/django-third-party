from django.contrib import admin

from .models import CustomContent


class CustomContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'path', 'active')
    list_filter = ('active', 'exact_match', 'partial_match')
    fieldsets = (
        (None, {'fields': ('title', 'path',)}),
        ('Settings', {'fields': (
            'active', 'exact_match', 'partial_match', 'header',)}),
        ('Content', {'fields': ('javascript', 'css')})
    )

    def activate(self, request, qs):
        qs.update(active=True)
    activate.short_description = 'Activate selected javascript'

    def deactivate(self, request, qs):
        qs.update(active=False)
    deactivate.short_description = 'Deactivate selected javascript'

    actions = (activate, deactivate)


admin.site.register(CustomContent, CustomContentAdmin)

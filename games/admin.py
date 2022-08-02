from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Game


class CustomGameAdmin(admin.ModelAdmin):
    model = Game
    fieldsets = (
        ('Owner', {
            'fields': ('rate',)
        }),
        ('Snack Info', {
            'fields': (
                'name',
                'desc'
            )
        })
    )

    list_display = ('name', 'rate')
    list_filter = ('name', 'desc')
    search_fields = ('name', 'desc')


admin.site.register(Game, CustomGameAdmin)

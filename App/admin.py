from django.contrib import admin

# Register your models here.
from App.forms import PeriodsForm
from App.models import Agreement, Periods


class PeriodsAdmin(admin.ModelAdmin):
    form = PeriodsForm

    list_display = ('agreement', "period_start", 'period_finish')
    search_fields = ["period_start"]

admin.site.register(Agreement)
admin.site.register(Periods, PeriodsAdmin)

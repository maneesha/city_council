from django.contrib import admin
from council.models import Councilperson, Term

class CouncilpersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'gender', 'race', 'birthdate')
    search_fields = ('last_name',)
    ordering = ('last_name',)

class TermAdmin(admin.ModelAdmin):
    #list_display = ('district', 'party', 'start_date', 'end_date', 'how_left_office', 'departed', 'councilperson', 'predecessor', 'successor')
    list_display = ('district', 'party', 'start_date', 'departed', 'how_left_office', 'councilperson', 'predecessor', 'successor')

    list_filter = ('district',)
    ordering = ('district',)

admin.site.register(Councilperson, CouncilpersonAdmin)
admin.site.register(Term, TermAdmin)

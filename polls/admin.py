from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']


admin.site.register(Poll, PollAdmin)
=======
>>>>>>> 4da71ad7af025505fafd1edca6cdd2e71717b09e

from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title__startswith', 'title', 'isbn')
    date_hierarchy = 'publication_date'
    list_filter = ('publisher', 'isbn', 'publication_date')
    list_display = ('title', 'publisher',)


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names', 'first_names')
    search_fields = ('last_names__startswith', 'first_names', 'last_names')


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)


def initialled_name(obj):
    initials = ''.join([name[0] for name in obj.first_names.split(' ')])
    return "{}, {}".format(obj.last_names, initials)

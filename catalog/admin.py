from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language


class BookInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'date_of_birth',
        'date_of_death',
    )
    fields = [
        'first_name',
        'last_name',
        ('date_of_birth', 'date_of_death')
    ]
    inlines = [BookInline]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'display_genre'
    )
    inlines = [BookInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )
    list_display = (
        'book',
        'status',
        'due_back',
        'id'
    )

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Language)



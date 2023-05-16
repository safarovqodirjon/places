from django.contrib import admin
from django.contrib.auth.models import Group
from city_app.models import Category, City, Place, Contact

admin.site.unregister(Group)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = ("id", "title", "description", "category", "address", "city")
    list_filter = ("title",)
    search_fields = ("title", "city")
    list_display_links = ("title",)
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    list_display_links = ("title",)


from django.contrib import admin
from city_app.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', 'created_at')
    list_display_links = ('title',)
    readonly_fields = ['created_at', ]
    list_per_page = 20
    ordering = ['id', ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

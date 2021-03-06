from django.contrib import admin
from .models import song
from .models import Artist
from django.http import HttpResponse
import csv


@admin.register(song)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "artist")
    list_filter = ("artist",)
    actions = ("export_as_csv",)

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
    export_as_csv.short_description = "Exportar"


   



@admin.register(Artist)
class Post2Admin(admin.ModelAdmin):
    list_display = ("name", "date_joined")

    





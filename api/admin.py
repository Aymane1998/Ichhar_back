from django.contrib import admin

from api.models import Demand, Creator,Video

# Register your models here.
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'integration_date', 'rating', 'total_videos')

    # def total_videos(self, obj):
    #     return obj.total_videos
    # total_videos.short_description = 'Total Videos'

admin.site.register(Demand)
admin.site.register(Creator, CreatorAdmin)
admin.site.register(Video)
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from .models import Gallery, Blog, Event, Carousal, TrustMember, TrustTeamMember, YouTubeVideo

admin.site.site_header = 'VOICE Trust administration'
admin.site.site_title = 'VOICE Trust'
admin.site.index_title = 'VOICE Trust'


admin.site.register(Gallery)
admin.site.register(Blog)
admin.site.register(Event)
admin.site.register(Carousal)
admin.site.register(TrustMember)
admin.site.register(TrustTeamMember)
admin.site.register(YouTubeVideo)
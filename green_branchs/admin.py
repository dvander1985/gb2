from django.contrib import admin

from green_branchs.models import Topic_plan, Entry_plan, Topic_rec, Entry_rec, Topic_prod, Entry_prod, Topic_activ, Entry_activ, Topic, Entry

admin.site.register(Topic_plan)
admin.site.register(Entry_plan)

admin.site.register(Topic_rec)
admin.site.register(Entry_rec)

admin.site.register(Topic_prod)
admin.site.register(Entry_prod)

admin.site.register(Topic_activ)
admin.site.register(Entry_activ)

admin.site.register(Topic)
admin.site.register(Entry)

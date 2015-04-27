from django.contrib import admin

from fembers.models import List, Member


class MemberAdmin(admin.ModelAdmin):
    exclude = ('number',)


class ListAdmin(admin.ModelAdmin):
    pass


admin.site.register(Member, MemberAdmin)
admin.site.register(List, ListAdmin)

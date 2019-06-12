from django.contrib import admin
from .models import Activity, Member

class MemberInline(admin.TabularInline):
    model = Member

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields  = ('name',)
    inlines = [MemberInline]

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'nid', 'department')
    fields  = ('name', 'nid', 'department', 'sex', 'birthday')

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Member, MemberAdmin)
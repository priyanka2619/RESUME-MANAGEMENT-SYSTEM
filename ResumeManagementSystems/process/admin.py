from django.contrib import admin
from django.contrib.auth.models import Group,User
from process.models import IndustriesModel

admin.site.register(IndustriesModel)


admin.site.unregister(Group)
admin.site.unregister(User)




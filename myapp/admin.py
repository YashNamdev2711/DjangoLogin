from django.contrib import admin

# Register your models here.
from . models import InsertMarks
from . models import Qaa
admin.site.register(InsertMarks)
admin.site.register(Qaa)
admin.site.site_header='Future Tutor Admin'
admin.site.index_title='Welcome User'
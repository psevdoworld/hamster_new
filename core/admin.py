from django.contrib import admin
from core.models import Code
# Register your models here.

"""
@admin.action()
def run(m, r, q):
    for c in q:
        c.run_code()
"""
class CodeAdmin(admin.ModelAdmin):
        actions = []

admin.site.register(Code, CodeAdmin)

from django.contrib import admin
from core.models import Code
# Register your models here.
from core.models import Solution, Homework, Example

"""
@admin.action()
def run(m, r, q):
    for c in q:
        c.run_code()
"""
class CodeAdmin(admin.ModelAdmin):
        actions = []

admin.site.register(Code, CodeAdmin)
admin.site.register(Solution)
admin.site.register(Homework)
admin.site.register(Example)
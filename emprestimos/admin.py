from django.contrib import admin
from .models import emprestimo

@admin.register(emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('id',)

from django.contrib import admin
from .models import *

# Register your models here.

class LowonganAdmin(admin.ModelAdmin):
    list_display = ('id', 'posisi', 'header_logo', 'logo', 'lokasi', 'kualifikasi', 'level_karir', 'tahun_pengalaman', 'kualifikasi_pendidikan', 'tipe_pekerjaan', 'lainnya', 'perusahaan', 'created_on')
    list_display_links = ('id', 'posisi', 'header_logo', 'logo', 'lokasi', 'kualifikasi', 'level_karir', 'tahun_pengalaman', 'kualifikasi_pendidikan', 'tipe_pekerjaan', 'lainnya', 'perusahaan')
    search_fields = (['id', 'posisi', 'header_logo', 'logo', 'lokasi', 'kualifikasi', 'level_karir', 'tahun_pengalaman', 'kualifikasi_pendidikan', 'tipe_pekerjaan', 'lainnya', 'perusahaan'])
    list_per_page = 25

class PerusahaanAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'lokasi', 'tentang', 'website')
    list_display_links = ('id', 'nama', 'lokasi', 'tentang', 'website')
    search_fields = [('id', 'nama', 'lokasi', 'tentang', 'website')]
    list_per_page = 25

admin.site.register(Lowongan, LowonganAdmin)
admin.site.register(Perusahaan, PerusahaanAdmin)
from django.db import models

# Create your models here.

class Lowongan(models.Model):
    posisi = models.CharField(max_length=40)
    header_logo = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    lokasi = models.CharField(max_length=30)
    kualifikasi = models.TextField(max_length=3000)
    level_karir = models.CharField(max_length=20)
    tahun_pengalaman = models.CharField(max_length=20)
    kualifikasi_pendidikan = models.CharField(max_length=20)
    tipe_pekerjaan = models.CharField(max_length=20)
    lainnya = models.CharField(max_length=40)
    perusahaan = models.ForeignKey('Perusahaan', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.posisi

class Perusahaan(models.Model):
    nama = models.CharField(max_length=40)
    lokasi = models.CharField(max_length=40)
    tentang = models.TextField(max_length=300)
    website = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nama
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField("Nama Course", max_length=200)
    description = models.TextField("Deskripsi", null=True, blank=True)
    price = models.IntegerField("Harga")
    image = models.ImageField("Banner", null=True, blank=True)
    teacher = models.ForeignKey(User, verbose_name="Pengajar", on_delete=models.RESTRICT)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Daftar Course"
    
    def __str__(self) -> str:
        return self.name+" : "+self.price
    
ROLE_OPTIONS = [('std', "Siswa"), ('ast', "Asisten")]

class CourseMember(models.Model):
    course_id = models.ForeignKey(Course, verbose_name="Matkul", on_delete=models.RESTRICT)
    user_id = models.ForeignKey(User, verbose_name="Siswa", on_delete=models.RESTRICT)
    roles = models.CharField("Peran", max_length=3, choices=ROLE_OPTIONS, default='std')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Subscriber Matkul"
        verbose_name_plural = "Subscriber Matkul"

    def __str__(self) -> str:
        return self.course_id+" : "+self.user_id

class CourseContent(models.Model):
    name = models.CharField("Judul Konten", max_length=200)
    description = models.TextField("Deskripsi", default='-')
    video_url = models.CharField('URL Video', max_length=200, null=True, blank=True)
    file_attachment = models.FileField("File", null=True, blank=True)
    course_id = models.ForeignKey(Course, verbose_name="Matkul", on_delete=models.RESTRICT)
    parent_id = models.ForeignKey("self", verbose_name="Induk", 
                                on_delete=models.RESTRICT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Konten Matkul"
        verbose_name_plural = "Konten Matkul"

    def __str__(self) -> str:
        return '['+self.course_id+"] "+self.name
    
class Comment(models.Model):
    content_id = models.ForeignKey(CourseContent, verbose_name="Konten", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, verbose_name="Pengguna", on_delete=models.CASCADE)
    comment = models.TextField('Komentar')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Komentar"
        verbose_name_plural = "Komentar"

    def __str__(self) -> str:
        return "Komen: "+self.content_id.name+"-"+self.user_id
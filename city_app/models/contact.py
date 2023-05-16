from django.db import models
from city_app.models import Place


class Contact(models.Model):
    phone = models.CharField("Номер телефона", max_length=20)
    additional_phone = models.CharField("Дополнительный номер телефона", max_length=24, null=True, blank=True)
    work_routine = models.CharField("График работы", max_length=100)
    email = models.EmailField("Почта", max_length=100)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    place = models.OneToOneField(Place, on_delete=models.CASCADE, related_name="contact")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"Контакты {self.place}"

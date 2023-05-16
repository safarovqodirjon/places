from django.db import models


class City(models.Model):
    title = models.CharField(
        verbose_name="Название города",
        max_length=100,
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.title

    def get_created_at_info(self):
        return f"Создано: {self.created_at.strftime('%d.%m.%Y')}"

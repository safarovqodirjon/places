from django.db import models


class Place(models.Model):
    title = models.CharField("Название заведения", max_length=250)
    description = models.TextField("Описание заведения", null=True)
    category = models.ForeignKey("city_app.category", on_delete=models.CASCADE,
                                 related_name="category", verbose_name="Категория заведения")
    address = models.CharField("Адрес заведения", max_length=255)
    city = models.ForeignKey("city_app.city", on_delete=models.CASCADE,
                             related_name="city", verbose_name="Город")

    class Meta:
        ordering = ["title"]
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"

    def __str__(self) -> str:
        return self.title

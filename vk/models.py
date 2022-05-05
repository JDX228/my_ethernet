from django.db import models


class Vk(models.Model):
    """Модель вк"""

    data_post = models.CharField("Дата публикации", max_length=20)
    text_post = models.TextField("Заголовок поста", unique=True)
    link_post = models.URLField("Ссылка на публикацию")
    link_image_post = models.URLField("Ссысылка на картинку")
    _is_expired = models.BooleanField(default=False)

    def hidden(pk):
        r = Vk.objects.get(pk=pk)
        r._is_expired = True
        r.save()

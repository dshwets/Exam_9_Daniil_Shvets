from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    photo_img = models.ImageField(upload_to='photos', verbose_name='Картинка')
    signature = models.CharField(max_length=200, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', related_name='author_photos',
                               on_delete=models.CASCADE)

    def is_in_favorite(self, user):
        liked_by_user = self.favorite_photo.filter(author=user)
        if liked_by_user.count() > 0:
            return True
        else:
            return False



class Favorite(models.Model):
    photo = models.ForeignKey(Photo,  verbose_name='Фото', related_name='favorite_photo', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name='author_favorites',
                               verbose_name='Автор', on_delete=models.CASCADE)

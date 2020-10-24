from django.urls import path, include

from webapp.views import IndexView, PhotoCreateView, PhotoView, PhotoUpdateView, PhotoDeleteView

app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/', include([
        path('add/', PhotoCreateView.as_view(), name='photo_create'),
        path('<int:pk>/', include([
            path('', PhotoView.as_view(), name='photo_view'),
            path('update/', PhotoUpdateView.as_view(), name='photo_update'),
            path('delete/', PhotoDeleteView.as_view(), name='photo_delete'),
            # path('add-to-cart/', CartAddView.as_view(), name='product_add_to_cart'),
        ])),
    ])),

]

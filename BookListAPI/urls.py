from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

router = DefaultRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
# urlpatterns = [
#     path('books', views.BookView.as_view(
#         {
#             'get': 'list',
#             'post': 'create',
#         })
#     ),
#     path('books/<int:pk>',views.BookView.as_view(
#         {
#             'get': 'retrieve',
#             'put': 'update',
#             'patch': 'partial_update',
#             'delete': 'destroy',
#         })
#     )
# ]

urlpatterns = router.urls

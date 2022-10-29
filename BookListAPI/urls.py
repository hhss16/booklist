from django.urls import path 
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('books', views.BookView,basename="books")
urlpatterns = [ 
    # path('books/',views.books) ,
    # path('books/',views.BookList.as_view()),
    # path('books/<int:pk>',views.Book.as_view())
    # path('books', views.BookView.as_view({'get':'list','post':'create'}))
    path('orders', views.Orders.listOrders)
] 

urlpatterns += router.urls
from os import name
from django.urls import path
from .views import HomeView,BookDetails,AddBookView, makeit,search_book,UpdateBook,ShowOrders,search_order
urlpatterns = [
    path('',HomeView.as_view(), name='Home'),
    path('Book/<int:pk>',BookDetails.as_view(), name='Detail'),
    path('add_Book/',AddBookView.as_view(), name='add_Book'),
    path('search_book', search_book , name='search-page'),
    path('Book/Update/<int:pk>' , UpdateBook.as_view(),name='Update-book'),
    path('makeorder/',makeit,name='op'),
    path('show_orders/',ShowOrders.as_view(),name='orders'),
    path('OrderSearch/',search_order,name='searchorder')
]
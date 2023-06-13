from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView
from .models import Book,Order
from django.http import HttpResponseRedirect
#def index(request):
    #return render(request, 'Home.html',{})
def search_book (request):
    if request.method == 'POST':
        searched = request.POST['searched']
        listtt = Book.objects.filter(Name__contains=searched)
        return render (request,'search_book.html' , {'searched':searched ,'listtt' :listtt })
    #else:    
       # return render (request,'search_book.html',{})

class HomeView(ListView):
    model =Book
    template_name ='Home.html'


class BookDetails(DetailView):
    model = Book
    template_name = 'BookDetails.html'

class AddBookView(CreateView):
    model= Book
    template_name = 'addBook.html'
    fields = '__all__'


class UpdateBook(UpdateView):
    model=Book
    template_name = 'Update_book.html'
    fields = '__all__'



class ShowOrders (ListView):
    model = Order
    template_name = 'orders.html'

def makeit (request):
    if request.method == 'POST':
        name = request.POST['name']
        op =   request.POST['op']
        username = request.POST['userr']
        new_entry = Order(UserName=username, BookName=name, Operation_needed=op)
        new_entry.save()
        return render (request,'confirm.html')

def search_order (request):
    if request.method == 'POST':
        searched = request.POST['searched']
        list1 = Order.objects.filter(UserName__contains=searched)
        return render (request,'search_order.html' , {'searched':searched ,'list1' :list1 })
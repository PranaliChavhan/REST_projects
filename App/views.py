from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView, CreateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import BookForm
from .models import Book

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

def Upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books':books})

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {'form': form})

def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

def delete_all(request):
    '''Delete all books'''
    all_books = Book.objects.all()
    for book in all_books:
        book.delete()
    return redirect("class_book_list")



class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'

class BookDelete(DeleteView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('class_book_list') 
from django.shortcuts import render
from django.http import HttpResponse
from bookstore_app.models import Books,Category

# Create your views here.
def index(request):
    return render(request,'bookstore_app/index.html')

def books(request):
    book_list=Books.objects.order_by('title')
    book_dict={'book_record':book_list}
    return render(request,'bookstore_app/books.html',context=book_dict)

def booksDetailView(request):
    book_list=Books.objects.all()
    book_dict={'book_record':book_list}
    return render(request,'bookstore_app/booksDetailView.html',context=book_dict)

def category_detail(request,name):
   category = Category.objects.POST.get(name = name)
   return render(request, 'category_detail.html',{'category':category})

'''def category_detail(request):
    fiction_books=Books.objects.filter(category='Fiction')
    fantasy_books=Books.objects.filter(category='Fantasy')
    programming_books=Books.objects.filter(category='Programming')
    biography=Books.objects.filter(category='Biography')
    children_books=Books.objects.filter(category='Children Books')
    sci_fi_books=Books.objects.filter(category='Science Fiction')
    return render(request,'category_detail.html', {'fiction_books':fiction_books,
                                                   'fantasy_books':fantasy_books,
                                                   'programming_books':programming_books,
                                                   'biography':biography,
                                                   'children_books':children_books,
                                                   'sci_fi_books':sci_fi_books
                                                   })'''
    

    


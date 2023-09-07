import email
from django.shortcuts import render,redirect
from .models import Product
from django.contrib import messages
import csv
from .forms import UploadCSVForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def index(request):
    data=Product.objects.all()
    context= {"data":data}
    return render(request,"index.html",context)

def login(request):
    return render(request,"login.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page or any other page after login
            return redirect('success_page')
        else:
            # Handle authentication failure, e.g., show an error message
            error_message = "Invalid email or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')



def register(request):
    return render(request,"register.html")

def product_review(request):
    data=Product.objects.all()
    context= {"data":data}
    return render(request,"product_review.html",context)

def product_view(request):
    data=Product.objects.all()
    context= {"data":data}
    return render(request,"product_view.html",context)

def insertData(request):
    if request.method=="POST":
        name = request.POST.get('name')
        barcode = request.POST.get('barcode')
        brand = request.POST.get('brand')
        description = request.POST.get('description')
        price = request.POST.get('price')
        available = request.POST.get('available')
        print(name,barcode,brand,description,price,available)
        query=Product(name=name,barcode=barcode,brand=brand,description=description,price=price,available=available)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/product_view")

    return render(request,"product_view.html")

def updateData(request,id):
    if request.method=="POST":
        name = request.POST.get('name')
        barcode = request.POST.get('barcode')
        brand = request.POST.get('brand')
        description = request.POST.get('description')
        price = request.POST.get('price')
        available = request.POST.get('available')

        edit=Product.objects.get(id=id)
        edit.name=name
        edit.barcode=barcode
        edit.brand=brand
        edit.description=description
        edit.price=price
        edit.available=available
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/product_view")
    d=Product.objects.get(id=id)
    context= {"d":d}
    return render(request,"product_review.html",context)


def deleteData(request,id):
    d=Product.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Successfully")

    return redirect("/product_view")


def index(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')

            # Assuming your CSV has a header row
            headers = next(csv_data)

            for row in csv_data:
                Product.objects.create(
                    name=row[0],
                    barcode=row[1],
                    brand=row[2],
                    description=row[3],
                    price=row[4],
                    available=row[5],
                    # Add more fields as needed
                )

            return redirect('product_view')

    else:
        form = UploadCSVForm()

    return render(request, 'index.html', {'form': form})



# def uploadWords(request):
#     up = request.POST.get('Upload') 
#     if up == "Upload":
#         if request.user.is_authenticated:
#             form = UploadFileForm()
#             if request.method == "POST":
#                  form = UploadFileForm(request.POST, request.FILES)
#                  if form.is_valid():
#                      file = request.FILES['file']
#                      usr = User.objects.get(username=request.user)
#                      if file.name.endswith(".csv"):
#                         reader = csv.reader(file)
#                         for row in reader:
#                            wt = WordsTable()
#                            wt.user = usr
#                            wt.word1 = row[0]
#                            wt.word2 = row[1]
#                            wt.word3 = row[2]
#                            wt.word4 = row[3]
#                            wt.word5 = row[4]
#                            wt.save()
#                 #         messages.success(request, "File uploaded successfully")
#                 #        return redirect("/")
#                 # else:
#                 #     messages.info(request, "File is not csv")
#                 #     return redirect("/")
#         context = {'form': form}
#         return render(request, "index.html", context)
#     else:
#         return redirect("index")

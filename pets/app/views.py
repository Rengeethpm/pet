from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Pet, Register
from app.forms import BuyerRegisterForm, PetRegisterForm


# Create your views here.

def home(request):
    return render(request, 'home.html')



def buyer_register(request):
    register_form = BuyerRegisterForm()
    if request.method == 'POST':
        register_form = BuyerRegisterForm(request.POST)
        if register_form.is_valid():
            user=register_form.save(commit= False)
            user.is_buyer = True
            user.save()
            print(user)
            return render(request, 'login_form.html')
        else:
            return HttpResponse("error")
    else:
        return render(request, 'buyer_register.html', {'register_form': register_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_buyer == True:
                return render(request, 'buyer_panel.html', {'user':user})
            if user.is_seller == True:
                return redirect(seller_panel)
        else:
            messages.info(request, 'INVALID CREDENTIALS')
    return render(request, 'login_form.html')


def buyer_panel(request):
    data = Pet.objects.all()
    context = {
        'pets': data
    }
    return render(request, 'buyer_panel.html', context)



# def pet_register(request):
#     data = Pet.objects.all()
#     if request.method == 'POST':
#         # pet_form = PetRegisterForm(request.POST)
#         # if pet_form.is_valid():
#         #     pet_form.save()
#         breed = request.POST['breed']
#         age = request.POST['age']
#         file = request.FILES['document']
#         data = Pet.objects.create(breed=breed, age=age, medical_certificate=file)
#         data.save()
#         # messages.info(request, 'The file is saved')
#         return HttpResponse("success")
#     else:
#         return render(request, 'pet_view.html', {'pets':data})


# def pet_update(request):
#     data = Pet.objects.get(id=id)
#     if request.method == 'POST':
#         breed = request.POST['breed']
#         age = request.POST['age']
#         file = request.FILES['document']
#         data = Pet.objects.create(breed=breed, age=age, medical_certificate=file)
#         if data.is_valid():
#             data.save
#             return redirect('pet_view')
#     else:

def pet_register(request):
    pet_form = PetRegisterForm
    if request.method == 'POST':
        pet_form = PetRegisterForm(request.POST,request.FILES)
        if pet_form.is_valid():
            pet = pet_form.save(commit=False)
            pet.save()
            return redirect('seller_panel')
    return render(request, 'pets_register.html', {'pet_form':pet_form})

def pet_view(request):
    pets = Pet.objects.filter()
    return render(request, 'pet_view.html', {'data': pets})

def pet_update(request, id):
    pets = Pet.objects.get(id=id)
    if request.method == 'POST':
        form = PetRegisterForm(request.POST or None, instance=pets)
        if form.is_valid():
            form.save()
            return redirect('seller_panel')
    else:
        form = PetRegisterForm(instance=pets)
    return render(request, 'pet_update.html',{'form':form})

def buyer_pet_view(request):
    data = Pet.objects.all()
    return render(request, 'buyer_pets_view.html',{'pets':data})

def seller_panel(request):
    data = Pet.objects.all()
    return render(request, 'seller_panel.html', {'pets':data})

def pet_delete(request,id ):
    pets = Pet.objects.get(id=id)
    if request.method == 'POST':
        pets.delete()
        return redirect('seller_panel')
    else:
        return redirect('seller_panel')

def Logout(request):
    logout(request)
    return redirect(home)

def buyer_profile(request,id):
    buyer = Register.objects.filter(id=id)
    print(buyer)
    return render(request, 'buyer_profile.html', {'buyer': buyer})

def pet_detail(request, pet_id):
    # Get the selected pet or return a 404 page if the pet doesn't exist
    pet = object.get(Pet, id=pet_id)

    context = {
        'pet': pet,
    }

    return render(request, 'pet_detail.html', context)



def purchase_pet(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)

        # Check if the pet is available for purchase
        if not pet.is_available:
            return render(request, 'pet_not_available.html')  # Create a template for this scenario

        user = request.user

        # Check if the user has enough funds to purchase the pet
        if user.balance < pet.price:
            return render(request, 'insufficient_funds.html')  # Create a template for this scenario

        # Deduct the pet's price from the user's account balance
        user.balance -= pet.price
        user.save()

        # Mark the pet as no longer available
        pet.is_available = False
        pet.save()

        # Create a purchase record
        purchase = Purchase(user=user, pet=pet)
        purchase.save()

        return render(request, 'purchase_success.html')  # Create a template for this scenario

    except Pet.DoesNotExist:
        return render(request, 'pet_not_found.html')  # Create a template for this scenario



































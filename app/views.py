from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BuyerRegisterForm, PetRegisterForm, BuyerEditForm
from .models import Pet, Register



# Create your views here.

def home(request):
    return render(request, 'home.html')



def buyer_register(request):
    register_form = BuyerRegisterForm()
    if request.method == 'POST':
        register_form = BuyerRegisterForm(request.POST)
        try:
            if register_form.is_valid():
                user=register_form.save(commit= False)
                user.is_buyer = True
                user.save()
                print(user)
                return render(request, 'login_form.html')
        except Exception as e:
            return HttpResponse(f"Error occurred during registration: {e}")
    else:
        return render(request, 'buyer_register.html', {'register_form': register_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = Register.objects.get(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_buyer == True:
                return render(request, 'buyer_panel.html', {'user': user})
            if user.is_seller == True:
                return redirect(seller_panel)
        else:
            messages.info(request, 'INVALID CREDENTIALS')
    return render(request, 'login_form.html')


def buyer_panel(request):
    user_data = request.user
    data = Pet.objects.all()
    print(user_data)
    context = {
        'pets': data,
        'user':user_data
    }
    return render(request, 'buyer_panel.html', context)





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

def buyer_update(request,id):
    customer = Register.objects.get(id=id)
    if request.method == 'POST':
        form = BuyerRegisterForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('buyer_panel')
    else:
        form = BuyerEditForm(instance=customer)
    return render(request,'buyer_update.html',{'form':form})




def buy_pet(request,id):
    # Retrieve the pet using its ID, or return a 404 error if not found
    pets = Pet.objects.get(id=id)

    if request.method == 'POST':
        # Handle the purchase process here, e.g., marking the pet as adopted
        if not pets.is_adopted:
            # Mark the pet as adopted (or set appropriate attributes)
            pets.is_adopted = True
            pets.save()
            # You can also associate the pet with the user who adopted it, if needed

            # Redirect to a confirmation page or any other appropriate page
            return render(request,'adoption_confirmation.html',{'pets':pets})  # Define this URL pattern
        else:
            # Pet is already adopted, handle this case appropriately
            return HttpResponse("This pet has already been adopted.")
    else:
        # Display the pet's details and a form to confirm the purchase
        return render(request, 'buy_pet.html', {'pets': pets})


def adoption_confirmation(request,id):
    pets = Pet.objects.filter(id=id)
    return render(request, 'adoption_confirmation.html',{'pets':pets})

































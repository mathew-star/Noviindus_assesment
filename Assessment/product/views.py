from django.shortcuts import render, redirect, get_object_or_404
from .models import Product,CartItem
from .forms import ProductForm
from django.contrib import messages

def add_product(request):
    """
    View to add a new product to the store.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_list')
        else:
            messages.error(request, 'Error adding product. Please correct the errors below.')
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})



def product_list(request):
    """
    View to display a list of all products.
    """
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})



def edit_product(request, product_id):
    """
    View to edit an existing product.
    """
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_list')
        else:
            messages.error(request, 'Error updating product. Please correct the errors below.')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/edit_product.html', {'form': form})

def delete_product(request, product_id):
    """
    View to delete a product from the store.
    """
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('product_list')



def add_to_cart(request, product_id):
    """
    View to add a product to the cart.
    """
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'{product.name} added to cart.')
    return redirect('cart')


def view_cart(request):
    """
    View to display the contents of the user's cart.
    """
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    total_quantity = sum(item.quantity for item in cart_items)

    return render(request, 'product/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_quantity': total_quantity,
    })


def remove_from_cart(request, cart_item_id):
    """
    View to remove a product from the cart.
    """
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, f'{cart_item.product.name} removed from cart.')
    return redirect('cart')

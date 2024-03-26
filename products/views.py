
#mtu asiguze hii pia

from django.http import JsonResponse
from .models import Item
from .serializers import ProductsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def product_list(request, format=None):

    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ProductsSerializer(items, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try:
        item = Item.objects.get(pk=id)
    except  Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



 # from django.shortcuts import render, get_object_or_404, redirect

# # Create your views here.

# from django.http import Http
# from .models import Category, Item


# def category(request):
#   """View for displaying all categories """
#   # Get the list of all categories in database
#   category=Category.objects.all()
  
#   return render(request,'category.html',{'categories':category})


# def detail(request,cat_id,item_id):
#     """ View to display individual item details"""
    
#     try:
#         cat = Category.objects.get(pk=cat_id)
#         item = Item.objects.get(pk=item_id)
        
#         context={'category':cat,'item':item}
#         return render(request,"detail.html",context)
#     except Exception as e:
#         print("Error getting data : ",e)
#         return redirect('category')


# def addItem(request):
#     if request.method == 'POST':
#       name = request.POST['name']
#       price = request.POST['price']
#       descrption = request.POST['description']  
      
#       new_item = Item(name=name, price=price, description=descrption)
#       new_item.save()
#       return redirect ('items',args=[new_item.category.id])
#     else:
#       cats = Category.objects.all()
#       return render(request,'addItem.html',{"cats":cats})


# def items(request,cat_id): 
#     """View to show all items in a specific category."""
#     try:  
#         current_category = Category.objects.get(pk=cat_id)
#         items = Item.objects.filter(category=current_category).order_by('-date')
#         context = {'category': current_category, 'items': items}
#         return render (request, "items.html", context)
#     except Exception as e:
#         print ("Category not found!")
#         return HttpResponseNotFound("<h2>Category Not Found</h2><p>The specified category does not exist.</p>")
#         return HttpResponseNotFound("<h2>No such category</h2>")

# @login_required
# def deleteItem(request,item_id):
#     item = get_object_or_404(Item, pk=item_id)
    
#     # Checking user is the owner of this item before deleting it.
#     if request.user != item.owner:
#         return HttpResponseForbidden("You do not have permission to delete this item.")
        
#     if request.method=='POST':
#         item.delete()
#         return redirect('home')
#     else: 
#         return render(request,"deleteItem.html",{'item':item})

# @login_required
# def editItem(request,item_id):
#     item = get_object_or_404(Item, pk=item_id)
    
#     # Checking user is the owner of this item before editing it.
#     if request.user != item.owner and not request.user.is_staff:
#         return HttpResponseForbidden("You  do not have permission to edit this item.")

#     form = EditItemForm(instance=item)

#     if request.method == 'POST':
#         form = EditItemForm(data=request.POST, files=request.FILES, instance=item)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.owner = request.user
#             item.save()
            
#             messages.add_message(request,messages.SUCCESS,'Your item has been updated successfully.')
#             return redirect('/items/'+str(item.pk))

#     context = {"form":form, "page":"edit"}    
#     return render(request,"items.html",context)    

# # This view returns a list of  all items in a given category that are for sale. It takes one parameter - the category id.
# # This view returns a list of all items in a given category. It takes one parameter - the category slug.
# def categoryView(request,category_slug):
#     try : 

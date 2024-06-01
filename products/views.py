from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from products.models import ProductModel, ProductCategoryModel, ProductColorModel, ProductTagModel, ProductManufacture


class ProductsListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'

    @staticmethod
    def change_colors_structure():
        colors = ProductColorModel.objects.all()
        colors_list = []
        temp_colors = []

        for color in colors:
            temp_colors.append(color)
            if len(temp_colors) == 2:
                colors_list.append(temp_colors)
                temp_colors = []  # Reset temp_colors to a new list after appending

        # Append any remaining colors in temp_colors if it is not empty
        if temp_colors:
            colors_list.append(temp_colors)

        return colors_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategoryModel.objects.all()
        context['manufactures'] = ProductManufacture.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['colors'] = ProductColorModel.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'products/product-detail.html'
    model = ProductModel
    context_object_name = 'product'


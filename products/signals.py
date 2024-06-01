# from django.db.models.signals import pre_save
# from django.dispatch import receiver
#
# from products.models import ProductModel
#
#
# @receiver(pre_save, sender=ProductModel)
# def product_updated(sender, instance, **kwargs):
#     if instance.is_discount():
#         instance.real_price = instance.price - (instance.discount * instance.price / 100)
#     else:
#         instance.real_price = instance.price

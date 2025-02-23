from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from cart.models import Coupon
from owner.models import Notifications
from cust.models import Usernotification
from .consumers import OrderNotificationConsumer
import re

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def send_notification_on_signup(sender,instance,created, **kwargs):
    pass
    # if created:
    #     channel_layer = get_channel_layer()
    #     group_name = 'user-notifications'
    #     event = {
    #         'type':'user_joined',
    #         'text':instance.email
    #     }
    #     async_to_sync(channel_layer.group_send)(group_name,event)
        
@receiver(post_save, sender=Coupon)
def send_notification_on_coupon_added(sender, instance, created, **kwargs):
    pass
    # if created:
    #     channel_layer = get_channel_layer()
    #     group_name = 'user-notifications'
    #     event = {
    #         'type': 'coupon_added',
    #     'coupon_code': f'Hurray! New coupon {instance.code} has been added.Grab it now✓',
    #     }
    #     async_to_sync(channel_layer.group_send)(group_name, event)
        
@receiver(post_save, sender=Notifications)      
def custom_notification(sender, instance, created, **kwargs):
    pass
    # if created:
    #     channel_layer = get_channel_layer()
    #     group_name = 'user-notifications'
    #     print(instance.content)
    #     event = {
    #         'type': 'custom_notification',
    #     'coupon_code': instance.content,
    #     }
    #     async_to_sync(channel_layer.group_send)(group_name, event)


# import re

@receiver(post_save, sender=Usernotification)
def order_notification(sender, instance, created, **kwargs):
    pass
    # if created:
    #     user_id = instance.user.id
    #     user_id_str = re.sub(r'[^a-zA-Z0-9]', '_', str(user_id))
    #     group_name = f"user_notifications_{user_id_str}"
    #     channel_layer = get_channel_layer()
    #     event = {
    #         'type': 'order_notification',
    #         'coupon_code': instance.content,
    #     }
    #     async_to_sync(channel_layer.group_add)(group_name, user_id_str)  # Use user_id_str as the channel_name
    #     async_to_sync(channel_layer.group_send)(group_name, event)



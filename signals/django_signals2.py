'''
Question 2: Do django signals run in the same thread as the caller? 
Please support your answer with a code snippet that conclusively proves your stance. 
The code does not need to be elegant and production ready, we just need to understand your logic.

'''

# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

class MySignal(models.Model):
    name = models.CharField(max_length=50)

#reciever decorator used and function beneath to reponse to corresponding post_save signal 
@receiver(post_save, sender=MySignal)
def example_handler1(sender, instance, **kwargs):
    print("Signal accepted for :", instance.name)
    print("Signal- example_handler1 thread ID:", threading.get_ident())

# Create an instance of MySignal
def create_instance():
    instance = MySignal.objects.create(name="Check")
    print("Instance created:", instance.name)
    print("Main thread ID:", threading.get_ident())

# Instace function called
create_instance()


#Output 
'''
Instance created: Check
Main thread ID: 123456789 (random)
Signal accepted for : Check
Signal- example_handler1 thread ID: 123456789

'''

''' 
Exp:
Same thread ID of signal handler and main thread indicates that django signals runs 
in the same thread as the caller.

threading.get_ident()- method used to generate thread Id.

'''

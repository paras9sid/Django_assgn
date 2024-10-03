'''
Question 3: By default do django signals run in the same database transaction as the caller? 
Please support your answer with a code snippet that conclusively proves your stance. 
The code does not need to be elegant and production ready, we just need to understand your logic.

'''

# models.py
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MySignal(models.Model):
    name = models.CharField(max_length=50)

#reciever decorator used and function beneath to reponse to corresponding post_save signal 
@receiver(post_save, sender=MySignal)
def example_handler1(sender, instance, **kwargs):
    print("Signal accepted for :", instance.name)
    # To check if a transaction is going on and we are in it!
    print("In transaction:", transaction.get_connection().in_atomic_block)

# Create an instance of MySignal inside a transaction in this case.
def create_instance():
    with transaction.atomic():
        instance = MySignal.objects.create(name="Check")
        print("Instance created:", instance.name)
        # To check if a transaction is going on and we are in it!
        print("In transaction:", transaction.get_connection().in_atomic_block)


# Instace function called
create_instance()


#Output 
'''
False - will be printed by signal handler ,upon checking our existence in transaction ,
and create instance function will print True.

'''

''' 
Exp:
By default django signals do not run in the same database transaction as the caller.

'''

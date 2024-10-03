'''
Question 1: By default are django signals executed synchronously or asynchronously?
Please support your answer with a code snippet that conclusively proves your stance. 
The code does not need to be elegant and production ready, we just need to understand your logic.

'''

# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MySignal(models.Model):
    name = models.CharField(max_length=50)

#reciever decorator used and function beneath to reponse to corresponding post_save signal 
@receiver(post_save, sender=MySignal)
def example_handler1(sender, instance, **kwargs):
    print("First Instance started")

# 2nd - reciever decorator used and function beneath to reponse to corresponding post_save signal 
@receiver(post_save, sender=MySignal)
def example_handler2(sender, instance, **kwargs):
    print("Second Instance started")

# Create an instance of MySignal
def create_instance():
    instance = MySignal.objects.create(name="Check")
    print("Instance created:", instance.name)

# Instace function called
create_instance()


#Output 
'''
Instance created: Check
First Instance started
Second Instance started

'''

''' 
Exp:
Synchronous - after first task fully executed and printed its output if any, only then second one will start and finish. One at a time.
in our above snippet - 'first instace started' will be printed first and when example_handler1 will finish only
then handler2 will execute and print its statement.

'''

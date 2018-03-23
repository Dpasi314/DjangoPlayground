from django.test import TestCase
from ModelExample.models import Contact
from django.db.models import QuerySet

# Create your tests here.
class ContactTests(TestCase):
    def test_str(self):
        contact = Contact(first_name="FirstName", last_name="LastName")
        self.assertEquals(str(contact), 'FirstName@LastName')

    def test_all(self):
        Contact.objects.create(first_name='Dante', last_name='Pasionek')
        Contact.objects.create(first_name='Denae', last_name='Pasionek')
        Contact.objects.create(first_name='Joe', last_name='Pasionek')

        contacts = Contact.objects.all()
        cs = []
        for c in contacts:
           cs.append(c.first_name)
        self.assertEquals(cs, ['Dante', 'Denae', 'Joe'])

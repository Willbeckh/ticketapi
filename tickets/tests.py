from .models import Ticket
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Ticket, Category


class UserViewSetTestCase(TestCase):
    def setUp(self):
        # Create a test client
        self.client = APIClient()

    def test_list_users(self):
        headers = {'Accept': 'application/json'}
        users_url = 'https://ticketapi.up.railway.app/endpoints/api/users/'
        # Send a GET request to the viewset's `list` action;
        response = self.client.get(
            users_url, headers=headers, format='json')

        # Verify that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        results = response.json()  # returns a dict

        # extract users list from the api json response
        users_list = results['results']

        # Verify that the response contains a list of users
        self.assertIsInstance(users_list, list)

    def test_register_user(self):
        # Create a new user
        user_data = {
            'email': 'testuser@gmail.com',
            'first_name': 'test',
            'last_name': 'user',
            'username': 'testuser',
            'password': 'c0de404!@',
            'password2': 'c0de404!@',
        }
        response = self.client.post(
            '/auth/register/', user_data, format='json')

        self.assertEqual(response.status_code, 201)

        # Assert that the new user was created and added to the database
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

        # set the user object as a class attr
        self.user = User.objects.get()


# test ticket object model
class TestTicketModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create test users
        cls.user = User.objects.create(
            username='test_user', password='12345')

        # create test categories
        cls.category = Category.objects.create(name='general')

    def test_create_ticket(self):
        # create ticket
        ticket = Ticket.objects.create(
            title='Test Ticket',
            user=self.user,
            content='testing content.',
            category=self.category,
        )

        self.assertEqual(ticket.title, "Test Ticket")
        self.assertEqual(ticket.user, self.user)
        self.assertEqual(ticket.content, "testing content.")
        self.assertEqual(ticket.category, Category.objects.get(name='general'))

        # ASSERT that new ticket was added to db
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Ticket.objects.get().title, 'Test Ticket')

    # test update
    def test_update_ticket(self):
        ticket = Ticket.objects.create(
            title='Test Ticket',
            user=self.user,
            content='testing content.',
            category=self.category,
        )

        # update the ticket
        ticket.title = "Updated Test Ticket"
        ticket.save()

        # get ticket
        updated_ticket = Ticket.objects.get(id=ticket.id)

        # assert that ticket has been update
        self.assertEqual(updated_ticket.title, 'Updated Test Ticket')

    def test_ticket_delete(self):
        # test delete method
        self.assertEqual(Ticket.objects.count(), 0)

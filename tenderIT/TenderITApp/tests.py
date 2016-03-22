#imports are in dictionary order
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from datetime import datetime

from .views.content_views import companies, projects
from .models import Company, Project


#Writing views tests

class TestContentViews(TestCase):

    def setUp(self):
        """
        Setting up objects for tests
        :return: None
        """
        #setting up request object
        self.request = RequestFactory()

        #creating user object
        self.user_obj = User(username='ria', password='uni123',
               email='ria@gmail.com')
        self.user_obj.save()

        #creating Company object
        self.company_obj = Company(
            user=self.user_obj,
            nationalID='12334',
            name='Oracle',
            street='1St Street',
            city='City',
            country='AS',
            postcode='98980',
            email='oracle@gmail.com',
            phone='998980912',
            website='www.oracle.com',
        )
        self.company_obj.save()

        #setting up Project object
        self.project_obj = Project(
            company=self.company_obj,
            title='Django Project',
            description='Hello welcome to java project',
            budget=150,
            currency='EUR',
            startDate=datetime.now(),
            endDate=datetime.now()
        )
        self.project_obj.save()

###########################################
# testing views
###########################################

    def test_companies(self):
        request = self.request.get('companies/')
        response = companies(request=request)

        self.assertEqual(
            response.status_code, 200, 'response should be equal to 200'
        )
        self.assertGreater(
            response.getvalue().rfind('Oracle'),
            0, 'Oracle Should present in database'
                           )

    def test_projects(self):
        request = self.request.get('projects/')
        response = projects(request=request)

        self.assertEqual(
            response.status_code, 200, 'response should be equal to 200'
        )
        self.assertGreater(
            response.getvalue().rfind('Django Project'),
            0, 'title should be django project - string type'
                           )


###########################################
# testing models
###########################################
    def test_company_model(self):
        obj = self.company_obj
        self.assertEqual(
            obj.user.username, 'ria', 'Name should be ria as logged by user'
        )
        self.assertIsInstance(obj.name, str, 'Company should be string')

    def test_user_abstract_model(self):
        """
        To check django builtin auth
        :return:
        """
        obj = self.user_obj
        self.assertEqual(
            obj.username, 'ria', 'Name should be ria as logged by user'
        )
        self.assertEqual(obj.email, 'ria@gmail.com', 'Email should also be same')

    def test_project_model(self):
        obj = self.project_obj
        self.assertEqual(
            obj.company.name, 'Oracle', 'Comapny is Oracle - string'
        )
        self.assertIsInstance(obj.budget, int, 'Budget always should be int')
import uuid

from model_mommy import mommy
from django.test import TestCase

from core.models import get_file_path


# command: coverage run manage.py test


class classGetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        testfile = get_file_path(None, 'test.png')
        self.assertTrue(len(testfile), self.filename)


class ServiceTestCase(TestCase):

    def setUp(self):
        self.service = mommy.make('Service')

    def test_str(self):
        self.assertEquals(str(self.service), self.service.service)


class RoleTestCase(TestCase):

    def setUp(self):
        self.role = mommy.make('Role')

    def test_str(self):
        self.assertEquals(str(self.role), self.role.role)


class EmployeeTestCase(TestCase):

    def setUp(self):
        self.employee = mommy.make('Employee')

    def test_str(self):
        self.assertEquals(str(self.employee), self.employee.name)


class FeatureTestCase(TestCase):

    def setUp(self):
        self.feature = mommy.make('Feature')

    def test_str(self):
        self.assertEquals(str(self.feature), self.feature.name)

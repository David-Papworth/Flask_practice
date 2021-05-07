import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Task

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
        SECRET_KEY='TEST_SECRET_KEY',
        WTF_CSRF_ENABLED=False,
        DEBUG=True,
        )
        return app

    def setUp(self):
        db.create_all()
        test_task = Task(description="Test the flask app")
        db.session.add(test_task)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_create_get(self):
        response = self.client.get(url_for('created'))
        self.assertEqual(response.status_code, 200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_complete_get(self):
        response = self.client.get(url_for('complete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_incomplete_get(self):
        response = self.client.get(url_for('incomplete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_tasks(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Test the flask app", response.data)

class TestCreate(TestBase):
    def test_create_task(self):
        response = self.client.post(url_for('created'),
        data=dict(description="Create a new task"),
        follow_redirects=True
        )
        self.assertIn(b"Create a new task", response.data)

class TestUpdate(TestBase):
    def test_update_task(self):
        response = self.client.post(url_for('update', id=1),
        data=dict(description="Update a task"),
        follow_redirects=True
        )
        self.assertIn(b"Update a task", response.data)

class TestDelete(TestBase):
    def test_delete_task(self):
        response = self.client.get(url_for('delete', id=1),
        follow_redirects=True
        )
        self.assertNotIn(b"Test the flask app", response.data)
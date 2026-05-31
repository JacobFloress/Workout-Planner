import os
import app
import unittest
import tempfile




class AppTestCase(unittest.TestCase):

    """ Init database that we do not have yet"""

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.testing = True
        self.app = app.app.test_client()
        with app.app.app_context():
            app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

class BodyParameters(AppTestCase):
    def test_missing_body_type(self):
        rv = self.app.post('/body_parameters', data=dict(
            weight='80',
            height='1.82',
        ), follow_redirects=True)
        assert b'All fields are required' in rv.data

    def test_negative_values_body_param(self):
        rv = self.app.post('/body_parameters', data=dict(
            weight='-80',
            height='-1.82',
            body_type='ectomorph'
        ), follow_redirects=True)
        assert b'Enter valid values for weight and height' in rv.data


class Experiences(AppTestCase):

    def test_high_experience(self):
        rv = self.app.post('/experience', data=dict(
            experience='Highly Experienced'
        ), follow_redirects=True)
        assert b'Highly Experienced' in rv.data

    def test_some_experience(self):
        rv = self.app.post('/experience', data=dict(
            experience='Some Experience'
        ), follow_redirects=True)
        assert b'Some Experience' in rv.data

    def test_not_experience(self):
        rv = self.app.post('/experience', data=dict(
            experience='Not Experienced'
        ), follow_redirects=True)
        assert b'Not Experienced' in rv.data

    def test_nothing_experience(self):
        rv = self.app.post('/experience', data=dict(
            experience='Select Experience'
        ), follow_redirects=True)
        assert b'Experience must be chosen' in rv.data

class Signup(AppTestCase):

    def test_sign_up(self):
        rv = self.app.post('/sign_up_submit', data=dict(
            username = 'yolo123',
            password = 'this_will_be_hashed',
            password_c ='this_will_be_hashed',
            email='yolo@gmail.com'
        ), follow_redirects=True)

        print(rv.text)
        # made sure data made it to login.html by making sure the flash message was sent
        assert b'Made New Account' in rv.data


    def test_login(self):

        rv = self.app.post('/sign_up_submit', data=dict(
            username='yolo123',
            password='this_will_be_hashed',
            password_c='this_will_be_hashed',
            email='yolo@gmail.com'
        ), follow_redirects=True)

        rv_login = self.app.post('/login_submit', data=dict(
            username = 'yolo123',
            password = 'this_will_be_hashed',

        ), follow_redirects=True)

        print(rv_login.text)

        assert b'Successful Login' in rv_login.data

class Forgot_Password(AppTestCase):

    def test_valid_fp(self):
        rv = self.app.post('/sign_up_submit', data=dict(
            username='yolo123',
            password='this_will_be_hashed',
            password_c='this_will_be_hashed',
            email='yolo@gmail.com',
        ), follow_redirects=True)
        rv = self.app.post('/valid_fp', data=dict(
            username='yolo123',
            email ='yolo@gmail.com'
        ), follow_redirects=True)

        print(rv.text)

        assert b'Sent Email' in rv.data

    def test_fp_submit(self):
        rv = self.app.post('/sign_up_submit', data=dict(
            username='yolo123',
            password='this_will_be_hashed',
            password_c='this_will_be_hashed',
            email='yolo@gmail.com',
        ), follow_redirects=True)
        rv = self.app.post('/valid_fp', data=dict(
            username='yolo123',
            email='yolo@gmail.com'
        ), follow_redirects=True)
        rv= self.app.get('/fp_submit', data=dict(
            name='yolo123'
        ))
        print(rv.text)
        assert b'None' in rv.data

class Profile_settings(AppTestCase):
    def test_profile(self):
        rv = self.app.post('/sign_up_submit', data=dict(
            username='yolo123',
            password='this_will_be_hashed',
            password_c='this_will_be_hashed',
            email='yolo@gmail.com',
        ), follow_redirects=True)
        rv_login = self.app.post('/login_submit', data=dict(
            username='yolo123',
            password='this_will_be_hashed',
            email ='yolo@gmail.com',
            experience = '1',
            goals = '1',
            body ='1',
            weight ='200',
            height ='16.5'

        ), follow_redirects=True)
        print(rv_login.data)

        rv_login = self.app.get('/workout')
        print(rv_login.data)
        rv_login = self.app.get('/profile')
        assert b'Entering Profile' in rv_login.data

    def test_profile_redo_info(self):
        rv_login = self.app.post('/sign_up_submit', data=dict(
            username='yolo123',
            password='this_will_be_hashed',
            password_c='this_will_be_hashed',
            email='yolo@gmail.com',
        ), follow_redirects=True)
        rv_login = self.app.post('/login_submit', data=dict(
            username='yolo123',
            password='this_will_be_hashed',
            email='yolo@gmail.com',
            experience='1',
            goals='1',
            body='1',
            weight='200',
            height='16.5'

        ), follow_redirects=True)
        print(rv_login.data)

        rv_login = self.app.get('/workout')
        print(rv_login.data)
        rv_login = self.app.get('/profile')
        rv =self.app.post('/profile_redo_info')
        print(rv.data)
        assert b'redo information here' in rv.data

    def test_submit_pass(self):
        rv_login = self.app.post('/sign_up_submit', data=dict(
            username='yolo123',
            password='this_will_be_hashed',
            password_c='this_will_be_hashed',
            email='yolo@gmail.com',
        ), follow_redirects=True)
        rv_login = self.app.post('/login_submit', data=dict(
            username='yolo123',
            password='this_will_be_hashed',
            email='yolo@gmail.com',
            experience='highly_experienced',
            goals='gain_muscle',
            body='1',
            weight='200',
            height='16.5'

        ), follow_redirects=True)
        print(rv_login.data)
        rv_login = self.app.get('/workout')
        print(rv_login.data)
        rv_login = self.app.get('/profile')
        rv_login = self.app.post('/submit_pass', data=dict(
            password='this_will_be_hashed',
            password_c='this_will_be_hashed'
        ), follow_redirects=True
        )
        print(rv_login.data)
        assert b'pass changed' in rv_login.data

#Tests to make sure that home page renders and that the user homepage renders when they log in
class HomePageTests(AppTestCase):
   def test_homepage_renders(self):
       response = self.app.get('/')
       self.assertEqual(response.status_code, 200)
       self.assertIn(b"Welcome to the Workouts Planner", response.data)


   def test_user_homepage_renders(self):
       with app.app.app_context():
           db = app.get_db()
           db.execute(
               """INSERT INTO users (id, username, password, email, experience, goals) VALUES (?, ?, ?, ?, ?, ?)""",
               (1, "testuser", "testpassword", "testuser@example.com", 2, 3),)
           db.commit()


       with self.app.session_transaction() as session:
           session['user_id'] = 1


       response = self.app.get('/workout')
       self.assertEqual(response.status_code, 200)
       self.assertIn(b"Your Weekly Workout Schedule", response.data)


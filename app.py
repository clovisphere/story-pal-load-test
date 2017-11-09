from locust import HttpLocust, TaskSet, task
import random
import uuid

HTTP_OK = 200

STUDENTS = [
    {
        'username': 'lela',
        'password': 'sumbalgsumbalg'
    }
]

GUARDIANS = [
    {
        'username': 'sumbalg2',
        'password': 'sumbal16'
    }
]


class StudentBehavior(TaskSet):
    """Simulate a 'student' user navigating the site"""

    def on_start(self):
        """called when a Locust start before any task is scheduled."""
        self.payload = random.choice(STUDENTS)

        with self.client.post('/student_login', data=self.payload, catch_response=True) as response:
            if response.status_code != HTTP_OK:
                response.failure('Login attempt failed')

    @task(3)
    def view_topic_cards(self):
        self.client.get('/student/{}/my_topic_cards'.format(self.payload['username']))

    @task(1)
    def view_letter_box(self):
        self.client.get('/student/{}/letter_box'.format(self.payload['username']))

    @task(2)
    def view_letter(self):
        self.client.get('/student/{}/letters'.format(self.payload['username']))


class GuardianBehavior(TaskSet):
    """Simulate a 'guardian' user navigating the site"""

    def on_start(self):
        """called when a Locust start before any task is scheduled."""
        self.payload = random.choice(GUARDIANS)

        with self.client.post('/guardian_login', data=self.payload, catch_response=True) as response:
            if response.status_code != HTTP_OK:
                response.failure('Login attempt failed')

    @task(5)
    def view_matches(self):
        self.client.get('/match')

    @task(5)
    def read_about_partnership(self):
        self.client.get('/partners')

    @task(3)
    def view_students(self):
        self.client.get('/guardian/{}/my_students'.format(self.payload['username']))

    @task(3)
    def view_groups(self):
        self.client.get('/guardian/{}/my_match_groups'.format(self.payload['username']))

    @task(1)
    def create_group(self):
        group_name = 'Test_Group_' + str(uuid.uuid4()).replace('-', '')

        data_set = {
            'create_text': group_name,
            'number_of_student_accounts[]': random.randint(1, 50),
            'birth_year[]': random.randint(9, 17)
        }

        uri = '/guardian/{}/create_multiple_students'.format(self.payload['username'])

        with self.client.get(uri, data=data_set, catch_response=True) as response:
            if response.status_code != HTTP_OK:
                response.failure('Attempt to create new group <{}> failed!'.format(group_name))

    @task(2)
    def create_student(self):
        student_name = 'Test_Student_' + str(uuid.uuid4()).replace('-', '')
        names = [
            'Leyla',
            'Elvis',
            'John',
            'Marc',
            'Loulou',
            'Indira',
            'Shai'
        ]

        data_set = {
            'student[username]': student_name,
            'student[first_name]': random.choice(names) + '_' + str(random.randint(200, 888))
        }

        with self.client.post('/students', data=data_set, catch_response=True) as response:
            if response.status_code != HTTP_OK:
                response.failure('Attempt to create new student <{}> failed!'.format(student_name))


class StudentUser(HttpLocust):
    task_set = StudentBehavior
    min_wait = 5000  # min wait time between executing tasks
    max_wait = 9000  # max wait time between executing tasks


class GuardianUser(HttpLocust):
    task_set = GuardianBehavior
    min_wait = 5000  # min wait time between executing tasks
    max_wait = 9000  # max wait time between executing tasks

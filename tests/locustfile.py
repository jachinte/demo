from locust import HttpUser, task

class MyUser(HttpUser):

    @task
    def visit_homepage(self):
        self.client.get("/")

    @task
    def visit_installation(self):
        self.client.get("/en/stable/installation.html")

    @task
    def visit_quickstart(self):
        self.client.get("/en/stable/quickstart.html")


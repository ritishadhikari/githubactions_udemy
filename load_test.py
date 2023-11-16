from locust import HttpUser, between, task

class MyUser(HttpUser):
    # Setting a wait time of between two numbers
    wait_time=between(min_wait=5,max_wait=15)

    @task
    def get_posts(self):
        self.client.get("/posts")
    
    @task
    def get_users(self):
        self.client.get(url="/users")
    
    @task
    def create_post(self):
        data={
            "title":"NEW POST",
            "body":"This is a new post",
            "userId":1
        }
        headers={"Content-Type":"application/json"}
        self.client.post(url="/posts",json=data,headers=headers)
from locust import HttpUser, task


class ApiUser(HttpUser):

    @task
    def check_health(self):
        self.client.get(
            "http://ec2-35-180-228-111.eu-west-3.compute.amazonaws.com:5000/health_check")

    @task
    def predict(self):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'PRG': 100,
            'PL': 150,
            'PR': 120,
            'SK': 130,
            'TS': 140,
            'M11': 16,
            'BD2': 170,
            'Age': 30,
            'Insurance': 200
        }
        self.client.post(
            "http://ec2-35-180-228-111.eu-west-3.compute.amazonaws.com:5000/predict/patient",
            json=data,
            headers=headers
        )

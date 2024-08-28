class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User with {self.name} currently works as {self.current_job_title} can be reached out at this email {self.email}")


finding_user_one = User("krishnans.blr@gmail.com", "Krishnan", "pwd1", "QA director")
finding_user_one.get_user_info()

finding_user_two = User("krishnans@gmail.com", "John", "pwd2", "SQA director")
finding_user_two.get_user_info()


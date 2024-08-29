from user import User
from post import Post
finding_user_one = User("krishnans.blr@gmail.com", "Krishnan", "pwd1", "QA director")
finding_user_one.get_user_info()

finding_user_two = User("krishnans@gmail.com", "John", "pwd2", "SQA director")
finding_user_two.get_user_info()

first_post = Post("on a secret mission today", "Krishnan")
first_post.get_post_info()

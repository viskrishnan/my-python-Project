import requests

response = requests.get("https://github.com/api/v4/users/viskrishnan/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} Project URL: {project['web_url']}")
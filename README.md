# github_actions_1
Test App and Deploy with GitHub Actions

docker build -t flask_app:v0.2 .
########
docker run -d -p 5000:5000 flask_app:v0.2 
# flask_mysite

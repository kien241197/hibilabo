# HIBILABO SYSTEM
# Generate the requirements.txt file
	- pip freeze > requirements.txt
# Install dependencies from requirements.txt
	- pip install -r requirements.txt
# Migrate DB
	- python3 manage.py migrate
# Make supper user admin
	- python3 manage.py createsuperuser

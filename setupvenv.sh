# creating virtual environment in python and installing modules

# 1: Install virtualenv
sudo pip install virtualenv

# 2: Create virtualenv
virtualenv -p python3.6 venv 

# 3: Activate virtualenv
source venv/bin/activate 

# 4: install modules
pip install django

# 5: use deactivate to exit venv
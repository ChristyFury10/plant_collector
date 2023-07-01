# install dependencies
pip install -r deps.txt

# run migration
python manage.py migrate

# collect static files
python manage.py collectstatic
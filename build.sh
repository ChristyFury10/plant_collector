# install dependencies
pip install -r deps.txt

#collect static files
python manage.py collectstatic --no-input

# run migration
python manage.py migrate


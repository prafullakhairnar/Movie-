# Movie-
# Movie Rating System API

## Setup

```bash
git clone <your-repo>
cd movie_rating_project
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

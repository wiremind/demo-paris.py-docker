FROM tiangolo/uwsgi-nginx-flask:python3.5-index

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY static static

COPY uwsgi.ini ./uwsgi.ini

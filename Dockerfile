FROM zostaw/multiarch-numpy-base:latest

EXPOSE 8080

RUN apk --update add bash vim g++ gcc musl-dev linux-headers
RUN apk add --no-cache build-base libffi-dev
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

# Install requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# URL under which static (not modified by Python) files will be requested
# They will be served by Nginx directly, without being handled by uWSGI
ENV STATIC_URL /static
# Absolute path in where the static files wil be
ENV STATIC_PATH /app/static

# If STATIC_INDEX is 1, serve / with /static/index.html directly (or the static URL configured)
# ENV STATIC_INDEX 1
ENV STATIC_INDEX 0

# Add app
COPY ./app /app
WORKDIR /app

# Make /app/* available to be imported by Python globally to better support several use cases like Alembic migrations.
ENV PYTHONPATH=/app

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080", "--cert", "cert.pem", "--key", "key.pem"]

FROM zostaw/numpy:python-numpy-1.0

RUN apk --update add bash vim g++ gcc musl-dev linux-headers
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

# Install requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN mkdir ~/.ssh
RUN echo "Host *" >> ~/.ssh/config
RUN echo "StrictHostKeyChecking no" >> ~/.ssh/config

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
COPY ./learning_words /app/

# Make /app/* available to be imported by Python globally to better support several use cases like Alembic migrations.
ENV PYTHONPATH=/app

# Move the base entrypoint to reuse it
#RUN mv /entrypoint.sh /uwsgi-nginx-entrypoint.sh
# Copy the entrypoint that will generate Nginx additional configs
#COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh

#ENTRYPOINT ["/entrypoint.sh"]

# Run the start script provided by the parent image tiangolo/uwsgi-nginx.
# It will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start Nginx and uWSGI
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]

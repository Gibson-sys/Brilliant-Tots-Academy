FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libsasl2-dev \
    libldap2-dev \
    libjpeg-dev \
    libffi-dev \
    libssl-dev \
    git \
    && apt-get clean

# Install Odoo requirements
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy Odoo source code
COPY . /app/
WORKDIR /app

# Start Odoo using environment variables
CMD ["python3", "odoo-bin",
     "--db_host", "${DB_HOST}",
     "--db_port", "${DB_PORT}",
     "--db_user", "${DB_USER}",
     "--db_password", "${DB_PASSWORD}",
     "--addons-path", "addons,odoo/addons",
     "--log-level", "info",
     "-c", "/app/odoo.conf"]

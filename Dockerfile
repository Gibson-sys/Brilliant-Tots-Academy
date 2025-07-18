FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

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

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8069

# ✅ Shell form allows environment variables to expand
CMD bash -c "python3 odoo-bin --db_host=$DB_HOST --db_port=$DB_PORT --db_user=$DB_USER --db_password=$DB_PASSWORD --addons-path=addons,odoo/addons --log-level=info -c /app/odoo.conf"


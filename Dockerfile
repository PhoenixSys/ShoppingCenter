FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /ariana
COPY requirements.txt /ariana/
RUN pip install -r requirements.txt
COPY . /ariana/
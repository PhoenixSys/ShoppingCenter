FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . /ariana/

EXPOSE 8000

CMD ["gunicorn" , "ShoppingCenter.wsgi" , ":8000"]
FROM python:3.11-alpine
WORKDIR /Stripe
COPY ./ /Stripe
RUN apk update && pip install -r /Stripe/requirements.txt --no-cache-dir
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
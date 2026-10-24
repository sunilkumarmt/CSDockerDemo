FROM python:3.12-alpine

WORKDIR /app
COPY app.py .

# Render supplies PORT at runtime; the app defaults to 10000.
EXPOSE 10000

CMD ["python", "app.py"]

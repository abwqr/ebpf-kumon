# Use the official Python image as the base image
FROM python:3.9-slim
RUN pip install flask
COPY metrics.py .
EXPOSE 8000
CMD ["python3", "metrics.py"]


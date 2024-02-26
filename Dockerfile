# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /pixelvision

# Copy the requirements file and install dependencies
COPY requirements.txt /pixelvision/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY . /pixelvision/

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

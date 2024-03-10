# Use a specific Python version
FROM python:3.9.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy just the requirements file first to leverage Docker cache
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /code/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run Django migrations when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

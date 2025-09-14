FROM belam443/python-base:latest

# Set workdir inside container
WORKDIR /app

# Copy requirements first (for layer caching)
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copy only backend folder
COPY backend/ /app/

# Expose Django port
EXPOSE 8000

# Dev server with autoreload
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

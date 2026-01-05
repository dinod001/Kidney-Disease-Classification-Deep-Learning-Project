FROM tensorflow/tensorflow:2.12.0

# Set working directory
WORKDIR /app

# Tell Python to look for modules here
ENV PYTHONPATH=/app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the project
COPY . .
RUN pip install .

# Expose port
EXPOSE 8080

# Run API
CMD ["python", "app.py"]

FROM python:3.10-slim

RUN apt-get update && apt-get install curl -y

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

RUN curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  -o mc
RUN chmod +x mc

# Copy the application code
COPY . .


# Set the entrypoint
ENTRYPOINT ["./run.sh"]
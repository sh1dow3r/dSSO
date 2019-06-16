# Use an official Python runtime as an image
FROM python:3.6

# The EXPOSE instruction indicates the ports on which a container # # will listen for connections
EXPOSE 1800

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this
# instruction creates a directory with this name if it doesn’t exist
WORKDIR /api

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt /api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run mainAPI.py when the container launches
COPY . /app
CMD python mainAPI.py
# Use an official Python runtime as an image
FROM python:3.6

# The EXPOSE instruction indicates the ports on which a container # # will listen for connections
EXPOSE 1800

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this
# instruction creates a directory with this name if it doesn’t exist
WORKDIR /api

# Install any needed packages specified in requirements.txt
#COPY ./requirements.txt /api/requirements.txt

#upgrade pip to avoid future issues, installing requirements
COPY . /api/
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

#setting up environment variables for docker and flask
#ENV FLASK_APP mainAPI.py
#ENV FLASK_RUN_HOST 0.0.0.0

# Run mainAPI.py when the container launches
CMD make /api
CMD python /api/mainAPI.py



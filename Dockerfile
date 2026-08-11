# Let start building the Dockerfile 

#==============STAGE 1 BUILDER=============#

FROM python:3.12-slim as builder

# Let prevent python from wrting buffer files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Let now install our dependencies
RUN apt-get update && apt-get upgrade -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Let install dependencies 
COPY requirements.txt .
RUN pip install  --no-cache-dir --prefix=/install  -r requirements.txt     


#==============STAGE 2 FINAL RUNTIME=============#

FROM python:3.12-slim

WORKDIR /app

# Let copy only the install package for our building 
COPY --from=builder /install /usr/local

# Let copy our application code
COPY ./app ./app 

# Now let define our non-root user for secuity purpose
RUN useradd -m Bruce
USER Bruce

EXPOSE 8000

# Command to run our app 
CMD [ "uvicorn","app.main:app","--host","0.0.0.0","--port","8000" ]
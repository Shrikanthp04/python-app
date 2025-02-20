FROM python:3.12-alpine
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4000
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=4000"]

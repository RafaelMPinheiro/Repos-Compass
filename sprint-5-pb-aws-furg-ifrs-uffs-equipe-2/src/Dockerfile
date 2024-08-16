FROM python

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "python3", "main.py", "runserver", "0.0.0.0:8080" ]
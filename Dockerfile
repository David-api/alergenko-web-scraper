FROM python:3.9

WORKDIR /webScrapper

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "Main.py"]
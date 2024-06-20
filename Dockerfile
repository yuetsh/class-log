FROM python:3.12-alpine

WORKDIR /app

EXPOSE 8000

COPY requirements.txt /app

RUN pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD [ "sh", "/app/entrypoint.sh" ]
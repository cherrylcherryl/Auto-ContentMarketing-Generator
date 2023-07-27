FROM python:3.11.4-slim-bullseye

ENV OPENAI_API_KEY=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
ENV SERPER_API_KEY=e7ce86460e7210bef65bf76c1b4432800c9152dc

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get install -y netcat gcc

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
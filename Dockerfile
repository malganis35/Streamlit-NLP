FROM python:3.9-slim
LABEL maintainer="Cao Tri DO"

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "./app/app_sentiment.py", "--server.port=8501", "--server.address=0.0.0.0"]

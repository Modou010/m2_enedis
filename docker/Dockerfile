FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r streamlit/requirements.txt
CMD ["streamlit", "run", "streamlit/app.py"]

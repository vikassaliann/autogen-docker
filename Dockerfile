FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV OPENAI_API_KEY="OPEN_API_KE"
CMD ["python", "my_autogen_script.py"]
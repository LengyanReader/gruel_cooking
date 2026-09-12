FROM python:3.12-slim

ENV PYTHONIOENCODING=utf-8 \
    PYTHONUNBUFFERED=1 \
    LH_PORT=18080

WORKDIR /srv/living_heritage

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY data/seeds ./data/seeds
COPY scripts ./scripts

EXPOSE 18080

# boot() = init DB -> seed if empty -> serve (app/boot.py)
CMD ["python", "-m", "app.main"]
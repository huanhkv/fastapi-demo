FROM python:3.10.15-slim-bookworm

ARG CPU_LIMIT

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN useradd -m -u 1539 -o -s /bin/bash nonroot

RUN chown -R nonroot /app

USER nonroot

EXPOSE 8500

ENTRYPOINT ["/bin/bash", "-c", "fastapi run app/main.py --host 0.0.0.0 --port 8500 --workers $((CPU_LIMIT*2+1))"]
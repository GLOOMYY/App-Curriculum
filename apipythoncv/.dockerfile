FROM python:3-alpine AS builder
 
WORKDIR /apipythoncv
 
RUN python3 -m venv venv
ENV VIRTUAL_ENV=/apipythoncv/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
 
COPY req.txt .
RUN pip install -r req.txt
 
# Stage 2
FROM python:3-alpine AS runner
 
WORKDIR /apipythoncv
 
COPY --from=builder /app/venv venv
COPY example_django example_django
 
ENV VIRTUAL_ENV=/apipythoncv/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PORT=8000
 
EXPOSE ${PORT}
 
CMD gunicorn --bind :${PORT} --workers 2 example_django.wsgi
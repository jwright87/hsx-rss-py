FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
COPY . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app/hsx_rss_py
EXPOSE 80
CMD ["python","hsx_rss_api.py"]
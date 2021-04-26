FROM python:3

WORKDIR /usr/src/app/pass_gen

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y locales && apt-get install -y nano && python -m pip install Django && apt-get install -y nginx
RUN pip install uwsgi
RUN /etc/init.d/nginx start
RUN ln -s /usr/src/app/pass_gen/pass_gen_nginx.conf /etc/nginx/sites-enabled/

# Locale
RUN sed -i -e \
  's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen \
   && locale-gen

ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8

# +Timezone (если надо на этапе сборки)
ENV TZ Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE pass_gen_engine.settings

COPY .. .
ENV PORT=8000
EXPOSE 8000
# CMD [ "python", "manage.py", "runserver", "127.0.0.1:8000" ]
CMD [ "uwsgi", "--module", "pass_gen_engine.wsgi:application", "--env", "DJANGO_SETTINGS_MODULE=pass_gen_engine.settings", "--master" ]
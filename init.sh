#!/usr/bin/env bash

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/dj_conf.py /etc/gunicorn.d/dj_conf.py
#gunicorn -c /etc/gunicorn.d/hello.py hello:app qwr
gunicorn -c /etc/gunicorn.d/dj_conf.py ask.wsgi:application
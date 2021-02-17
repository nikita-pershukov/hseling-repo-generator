FROM hseling/hseling-web-base:python3.6-alpine3.7 as build

LABEL maintainer="Boris Orekhov <info@linghub.ru>"

RUN mkdir /dependencies
COPY ./hseling_web_generator/requirements.txt /dependencies/requirements.txt
COPY ./hseling_web_generator/setup.py /dependencies/setup.py

RUN pip install -r /dependencies/requirements.txt

FROM hseling/hseling-web-base:python3.6-alpine3.7 as production

COPY --from=build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=build /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages

COPY --from=build /dependencies /dependencies

COPY ./hseling_lib_generator /dependencies/hseling_lib_generator
RUN pip install /dependencies/hseling_lib_generator

COPY ./hseling_web_generator/hseling_web_generator /app/hseling_web_generator
COPY ./hseling_web_generator/main.py /app/main.py

ENV HSELING_WEB_GENERATOR_SETTINGS="/app/hseling_web_generator/default_settings.py"

HEALTHCHECK CMD curl --fail http://localhost:8000/healthz || exit 1

EXPOSE 8000

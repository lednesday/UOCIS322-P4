FROM python:3.8
LABEL maintainer="noemail@website.domain"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod +x run_tests.sh
# TODO: don't I need to actually run the script?
# RUN ./run_tests.sh
ENTRYPOINT ["python"]
CMD ["flask_brevets.py"]

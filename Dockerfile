FROM python:3-alpine
RUN apk update
RUN apk add git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-FrancoQuiroga.git
WORKDIR /ajedrez-2024-FrancoQuiroga
RUN pip install -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.main" ]
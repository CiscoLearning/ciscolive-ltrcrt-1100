FROM python:3.9.19-bullseye

WORKDIR /root/

COPY requirements.txt ./
COPY testing.py ./

RUN pip install --no-cache-dir -r requirements.txt

ENV WEBEX_TOKEN=MDAzMDU5MDMtODE1Ni00MjUxLTkwYmMtYjc5NGUxMmIzNjhiNWUzNDI0OTEtZjll_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f
ENV WEBEX_ROOM=Y2lzY29zcGFyazovL3VzL1JPT00vYmQ1ZjhiODAtOWFjZS0xMWVlLWE2OGEtYWQzYWE4ZTg0MzAz

CMD [ "python", "./joke-and-post.py" ]
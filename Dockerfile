FROM python:3.11.5
ADD . .
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["main.py"]
# docker build -t chatgpt_proj .
# docker run -d -p 8080:80 chatgpt_proj
# docker tag chatgpt-project1 yourusername/chatgpt-project1
# docker push yourusername/chatgpt-project1
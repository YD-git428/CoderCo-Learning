from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = os.getenv('REDIS_PORT', 6379)
redis_password = os.getenv('REDIS_PASSWORD', 'my_paswd')

r = redis.StrictRedis(
    host=redis_host,
    port=redis_port,
    password='my_paswd',
    decode_responses=True 
)
@app.route('/')
def Welcome_page():
    return '''
  <html>
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Webpage_Background</title>
     <style>
      body {
         font-family: 'Century Gothic', sans-serif;
         text-align: center;
         background: rgb(2,0,36);
         background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 16%, rgba(0,212,255,1) 100%);
      }
     
     .btn {
        padding: 10px 20px;
        margin: 10px;
        font-size: 18px;
        color: black;
        text-weight: bold
        background-color: #1A466D;
        text-decoration-color: none;
        border-radius: 5px;
        border:5px groove #007BFF;
        cursor: pointer;
        }
            .btn:hover {
                background-color: #193B59;
            }
     
     </style>
    </head>
     <h1 class="body">Welcome to my First (ever) App</h1>
     <a href='/count' class="btn">Checkout more Quotes by Simply refreshing</a>
</html>
'''      

@app.route('/count')
def counter():
        count = r.incr('visits')
        return f"This site has been visited {count} times."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777)

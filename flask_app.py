#Opdracht 3
from flask import Flask

app=Flask[__name__]
if __name__ == '__main__':
    app.run(port=5000,debuf=True)

@app.route('/')
def home():
    return"<p>Welkom op mijn nieuwe site</p>"

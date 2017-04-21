from Flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hi Allen!"

if __name__ == "__main__":
    app.run()

    

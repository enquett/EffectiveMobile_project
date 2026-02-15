from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def response():
    return "Hello from Effective Mobile!"



if __name__ == '__main__':
    app.run(host='0.0.0.0')

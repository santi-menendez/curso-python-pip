# from os import name
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import store

app = FastAPI()


@app.get("/")
def get_list():
    return [
        1,
        2,
        3,
    ]


@app.get("/contact", response_class=HTMLResponse)
# @app.get("/contact")
def get_list():
    # return {"name": "Platzi"}
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """


def run():
    store.get_categories()


if __name__ == "__main__":
    run()

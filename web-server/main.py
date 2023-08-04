import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')       # Decorador
def get_list():
    return[1, 2, 3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>Hola Soy un Título</title>
        </head>
        <body>
            <h1>Hola Soy una página</h1>
            <p>soy un parrafo</p>
        </body>
    </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()

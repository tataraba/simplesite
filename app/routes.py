from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def index():
    return """
        <html>
            <head>
                <title>Simple Site</title>
            </head>
            <body>
                <h1>Hello World!</h1>
            </body>
        </html>
        """
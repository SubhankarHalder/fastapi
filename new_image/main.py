from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request, response_class=FileResponse):
#    return FileResponse("test.png")
    return templates.TemplateResponse("home.html", {
        "request": request, 
        "user_img": "test.png" 
    })

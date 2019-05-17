from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory='templates')

app = Starlette()
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.route("/")
def index(request):
    user_agent = request.headers.get("User-Agent")

    if user_agent == "NCSA_Mosaic/2.0 (Windows 3.1)":
        flag = "hsctf{wow_you_are_agent_keith_now}"
    else:
        flag = "Access Denied"

    template = "index.html"
    context = {"flag": flag, "user_agent": user_agent, 'request': request}
    return templates.TemplateResponse(template, context)

if __name__ == "__main__":
    uvicorn.run(app)

import asyncio
import uvicorn

from os.path import commonprefix

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates


flag = "hsctf{sm0l_fl4g}"


templates = Jinja2Templates(".")

app = Starlette()

@app.route("/", methods=["GET", "POST"])
async def index(request):
    if request.method == "POST":
        form = await request.form()

        password = str(form.get("password", ""))

        common = len(commonprefix((password, flag)))
        await asyncio.sleep(common * 0.5)

        incorrect = password != flag
        correct = password == flag
    else:
        incorrect = correct = False

    return templates.TemplateResponse("index.html", {"incorrect": incorrect, "correct": correct, "request": request})


if __name__ == "__main__":
    uvicorn.run(app)

# :sparkles:Building a Python-Backed Frontend with HTMX and TailwindCSS:sparkles:

### Table of Contents
| Branch | Chapter | Description
| --- | --- | --- |
| [`main`](https://github.com/tataraba/simplesite) | Preface | Getting Started
| [`01_templates`](https://github.com/tataraba/simplesite/tree/01_templates) | Chapter 1 | Using Jinja Templates to Render HTML
| [`02_tailwindcss`](https://github.com/tataraba/simplesite/tree/02_tailwindcss) | Chapter 2 | Harnessing TailwindCSS for Consistent Design
| [`03_tinydb`](https://github.com/tataraba/simplesite/tree/03_tinydb) | Chapter 3 | A Thin Database Layer
| [`01_htmx`](https://github.com/tataraba/simplesite/tree/04_htmx) | Chapter 4 | Modern Browser Features Directly from HTML

## 📚 Preface

The first step to get going is to build a minimal FastAPI application. If you have used other web frameworks before, you should be able to follow along. I recommend starting from scratch, but if you feel like skipping the formalities, you can also clone this template and move on to Chapter 1.

Otherwise, you'll want to follow these steps.

Create a project directory and create your virtual environment.

`python -m venv .venv`

Next, create an `app` directory and a `test` directory.

Also, create these files:

- `requirements.txt` - to keep track of your dependencies
- `.gitignore` - you should really plan to use version control, because why not?
- `README.md` - Write down some things you may want to remember later

Within your `app` directory, create the following files:

- `__init__.py` - makes your app a "package"
- `main.py` - where your FastAPI application will live
- `config.py` - for app configuration
- `routes.py` - here we will define our url endpoints or "views"

### Installing Your Dependencies

Next, you need to install the FastAPI and Uvicorn libraries. Additionally, you can also install pytest and httpx for testing purposes.

Open your `requirements.txt` file and type in the following:

```
fastapi
uvicorn[standard]
pytest
httpx
```

Next, make sure to activate your virtual environment and install your dependencies ([see above for more detail on installation](#installing)). The command to install from your requirements file is `python -m pip install -r requirements.txt`.

> Note: If you use a package manager, you could use the `pyproject.toml` file included in this template instead.

### Building Your App

Now that you have your structure set, create a basic FastAPI application within `main.py`

- It's okay, you can look at the code here and copy/paste

For all intents and purposes, you can go through this thing without a `config.py`. I have kept it here because it may be useful if you build out your app in the future. The most important pieces in there are the `STATIC_DIR` and `TEMPLATE_DIR` attributes that point to where our html templates and static files will live. But we'll touch more on that in Chapter 1.

The `FASTAPI_PROPERTIES` are just key:value pairs that we can pass to the `FastAPI` object. The most important piece in there is the `defaulet_response_class` that changes the default response type of your FastAPI application.

While most "Hello World" style FastAPI tutorials include their routes/views within the context of the application (i.e., in `main.py`), in practice, it's better to keep these elsewhere, which is why you created a `routes.py` file.

Routes in FastAPI look something like this:

```
@app.get("/")
def index_page():
  return SomeResponse
```

You'll notice that the `routes.py` file has a different decorator. This is what allows us to link our routes back to the app that we defined in `main.py`.

At the top of `routes.py`, we include `router = APIRouter()`. Now, all the routes that we define with the `@router` decorator will get added to the `APIRouter()` object defined here.

And in `main.py`, you can register all those routes directly to your application:

```
app.include_router(router)
```

### Running Your App

Once you have everything set up, you want to make sure that your app runs.

> Note: I haven't gone over setting up your tests in `pytest`, but take a look at the template to get an idea.

To start your app with the uvicorn server application, you'll need to type the following command:

```
uvicorn app.main:app
```

This is a `uvicorn` CLI command. The `app.main` represents the path to a module within your app, and the `:app` represents the object that you are calling (defined as `app = get_app()` in `main.py`).

If the command is successful, you can visit 127.0.0.1:8000 to see your app in all it's _Hello World_ glory.

Take your time getting comfortable with how your app is put together.

Once you're comfortable with how it works, it is time to move on to Chapter 1.
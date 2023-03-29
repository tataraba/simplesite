# :sparkles:Build a Python-Backed Frontend With HTMX and TailwindCSS:sparkles:

### Table of Contents
| Chapter | Title | Branch
| --- | --- | --- |
| Preface | [Getting Started](https://github.com/tataraba/simplesite/blob/main/docs/00_Preface.md) | [`main`](https://github.com/tataraba/simplesite) |
| Chapter 1 | [Using Jinja Templates to Render HTML](https://github.com/tataraba/simplesite/blob/main/docs/01_Chapter_1.md) | [`01_templates`](https://github.com/tataraba/simplesite/tree/01_templates) |
| Chapter 2 | [Harnessing TailwindCSS for Consistent Design](https://github.com/tataraba/simplesite/blob/main/docs/02_Chapter_2.md) | [`02_tailwindcss`](https://github.com/tataraba/simplesite/tree/02_tailwindcss) |
| Chapter 3 | [A Thin Database Layer](https://github.com/tataraba/simplesite/blob/main/docs/03_Chapter_3.md) | [`03_tinydb`](https://github.com/tataraba/simplesite/tree/03_tinydb) |
| Chapter 4 | [Modern Browser Features Directly from HTML](https://github.com/tataraba/simplesite/blob/main/docs/04_Chapter_4.md) | [`04_htmx`](https://github.com/tataraba/simplesite/tree/04_htmx)  |

## 📚 Preface: Getting Started

First of all. Welcome!

Thank you for stopping by. This document began as bullet points for a workshop, and let's just say it grew _a little_ beyond the initial scope.

My (time) loss, is your gain!

If you want to get started right away, feel free to clone the repo or select "Use this template."

This project is also set up to work with [GitHub Codespaces](https://github.com/features/codespaces).

> Note: GitHub Codespaces allows you to work in the cloud without setting up a local development environment. All dependencies are managed for you! All personal GitHub accounts include a monthly quota of 60 hours of free usage.

Once you have cloned the starter application, you are ready to move on to [Chapter 1](https://github.com/tataraba/simplesite/blob/main/docs/01_Chapter_1.md).

If you want to go the more traditional route, you can clone/copy to your local environment. If you're fairly new to web frameworks, I recommend starting from scratch, as it helps create a mental model of how all the pieces fit together.

### From Scratch

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

Next, make sure to activate your virtual environment and install your dependencies. The command to install from your requirements file is `python -m pip install -r requirements.txt`.

> Note: If you use a package manager, you could use the `pyproject.toml` file included in this template instead.

### Building Your App

Now that you have your structure set, create a basic FastAPI application within `main.py`

- It's okay, you can look at the code here and copy/paste

For all intents and purposes, you can go through this exercise without a `config.py`. I have kept it here because it may be useful if you build out your app in the future. The most important pieces in there are the `STATIC_DIR` and `TEMPLATE_DIR` attributes that point to where our html templates and static files will live. But we'll touch more on that in Chapter 1.

The `FASTAPI_PROPERTIES` are just _key:value_ pairs that we can pass to the `FastAPI` object. The most important piece in there is the `defaulet_response_class` that changes the default response type of your FastAPI application.

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

If the command is successful, you can visit [127.0.0.1:8000](http://127.0.0.1:8000) to see your app in all it's _Hello World_ glory.

Take your time getting comfortable with how your app is put together.

Once you're comfortable with how it works, it is time to move on to [Chapter 1](https://github.com/tataraba/simplesite/blob/main/docs/01_Chapter_1.md).
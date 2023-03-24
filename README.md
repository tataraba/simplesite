<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h2 align="center">Simple Site</h2>
<h3 align="center">Featuring htmx and TailwindCSS</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Creating a Python-backed front end, featuring FastAPI, htmx, and TailwindCSS.
    <br>
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [🏁 Getting Started ](#-getting-started-)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
- [🔧 Running the tests ](#-running-the-tests-)
- [🎈 Usage ](#-usage-)
- [🚀 Deployment ](#-deployment-)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)
- [🎉 Acknowledgements ](#-acknowledgements-)
- [Chapter 2](#chapter-2)
  - [Extra](#extra)

## 🧐 About <a name = "about"></a>

Build a beautiful web application using nothing more than Python, htmx, and TailwindCSS. Harness the power of Jinja templates and server-side rendering to create a dynamic, REST-ful web app.

## 🏁 Getting Started <a name = "getting_started"></a>

This repository was prepared as part of a workshop on how to create a python-backed front end, featuring Jinja templates for HTML rendering, TailwindCSS for style, and htmx for pizzazz! 😎

The main branch contains the "starter" app, which lacks all of the features. It only contains a basic FastAPI "Hello, World!" application. Each subsequent branch contains more features. If you want the fully-featured application, switch to the appropriate branch and select "Use This Template" (make sure to only clone the "current" branch).

### Prerequisites

Your only requirement is to have **Python 3.11** (or later) installed locally. The rest of the dependencies are in the `pyproject.toml` file, as well as the `requirements.txt` file.

> Why both? If you use a package manager (i.e., I use `pdm`), you can use your package manager to install dependencies from the `pyproject.toml`. Otherwise, you can go the more traditional route using the `requirements.txt` file.

### Installing

If you have a package manager, you can use that to install directly from the `pyproject.toml` file. Otherwise, you can go the traditional rout (see below).

After cloning the repo locally, you will need to create a virtual environment. Navigate to the location where you have cloned the project and run the following command:

```
python -m venv .venv
```

This will create a `.venv` directory within your project.

Next, activate your environment:

```
# On Windows
.\.venv\Scripts\activate

# On MacOS/Linux
$ source myvenv/bin/activate
```

Then, install the requirements:
```
python -m pip install -r requirements.txt
```


## 🔧 Running the tests <a name = "tests"></a>

After activating your virtual environment, you can run tests by typing `pytest` on the command line.

```
pytest
```

If everything has gone well so far, all tests should pass.

## 🎈 Usage <a name="usage"></a>

This repo was created primarily to aid in a workshop setting, so your mileage may vary. Feel free to clone the repo and make it your own. But most of all, have fun! 🥳

## 🚀 Deployment <a name = "deployment"></a>

- Coming Soon

## ⛏️ Built Using <a name = "built_using"></a>

- FastAPI
- Jinja2
- TailwindCSS
- HTMX


## ✍️ Authors <a name = "authors"></a>

- [@tataraba](https://github.com/tataraba) - Mario Munoz, _Python By Night_


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Coming soon


## Chapter 2

- `pip install tailwindcss`
- Gives you the `tailwindcss` command in your terminal
- Navigate to project root and type `tailwindcss`
  - should confirm that binary is being downloaded
  - then the help menu should be available
- Type `tailwindcss init`
  - this creates a `tailwind.config.js` file
  - This is where you tell tailwind where to look for your html files
  - can be a regex pointing to your template directory and file type
- Next, need to create/edit file with tailwind directives
  - typically in a 'src' directory used for compilation
  - create `app/static/src/tw.css` and add:
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```
- Then, run CLI command to scan template folder (defined in tailwind.config.js)
  - `tailwindcss -i ./src/tw.css -o ./dist/main.css --watch`
  - This compiles from tw.css into main.css (will overwrite what was there)
  - Use the `--watch` argument for a watcher that compiles on save
  - Use the `--minify` argument when compiling to production
- Tailwind extension in your code editor will make life easier
  - Otherwise, have the tailwindcss website open

### Extra
- Can use the `subprocess.run` command to run command on app startup
  - will force tailwind compilation on app startup in case you forget
- When starting app with uvicorn, can use the `--reload-include *.html` to watch changes in templates directory
  - slower compiler than having a separate process, but won't have to remember to start tailwind process
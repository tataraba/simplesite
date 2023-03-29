# :sparkles:Build a Python-Backed Frontend With HTMX and TailwindCSS:sparkles:

### Table of Contents
| Chapter | Title | Branch
| --- | --- | --- |
| Preface | [Getting Started](https://github.com/tataraba/simplesite/blob/main/docs/00_Preface.md) | [`main`](https://github.com/tataraba/simplesite) |
| Chapter 1 | [Using Jinja Templates to Render HTML](https://github.com/tataraba/simplesite/blob/main/docs/01_Chapter_1.md) | [`01_templates`](https://github.com/tataraba/simplesite/tree/01_templates) |
| Chapter 2 | [Harnessing TailwindCSS for Consistent Design](https://github.com/tataraba/simplesite/blob/main/docs/02_Chapter_2.md) | [`02_tailwindcss`](https://github.com/tataraba/simplesite/tree/02_tailwindcss) |
| Chapter 3 | [A Thin Database Layer](https://github.com/tataraba/simplesite/blob/main/docs/03_Chapter_3.md) | [`03_tinydb`](https://github.com/tataraba/simplesite/tree/03_tinydb) |
| Chapter 4 | [Modern Browser Features Directly from HTML](https://github.com/tataraba/simplesite/blob/main/docs/04_Chapter_4.md) | [`04_htmx`](https://github.com/tataraba/simplesite/tree/04_htmx)  |

## 📚 Chapter 3: A Thin Database Layer

Before diving into htmx, take a step back to think about what we're trying to accomplish.

When a user of your application submits a request, your web app (FastAPI) decides what response to send back to the user.

This interaction is handled entirely in the back end. By using htmx, you have access to AJAX requests from any element in your HTML. These requests correspond to these attributes that you may be familiar with: `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.

These AJAX requests can now be handled by your back end code (FastAPI)&mdash;the associated processing all accomplished on the back end&mdash;before being sent back as a response to the front end.

In order to truly appreciate much of the functionality of htmx, I wanted to simulate what most applications might be doing on the back end: namely, interacting with a database.

Regardless of what ORM (Object Relational Mapper) or ODM (Object Document Mapper) you choose to use, the idea is the same. You are sent a request, which then processes a database call matching that request. The database operation produces data, which is then sent back as a response to the user.

That response can be wrapped up in the template "context" and sent to the user.

> Note: Even if you're a little unclear on all the gibberish above, don't distress. Just try to picture the "workflow" of a web request: A user makes a request (i.e., clicks a link) that gets sent to your web app; your app makes a database call based on that request; the response from the database gets sent back to your templates; the templates render the response for the user.

### TinyDB

The TinyDB library provides a tiny, document-oriented database that is stored locally (similar to sqlite).

It is being used here to simulate a database layer without the need of an external server or any other PyPI dependency. But mostly, since the storage layer is document-based and represented as a Python `dict` object, Python developers will already have familiarity with the database responses.

The API is already very easy to understand. However, I've created a new module (`crud.py`) that contains a thin wrapper class (`CRUD`). This class allows you to perform some basic commands:

- `all_items()` - return a lits of all items in the database (a `list` of `dict` items)
- `find(key, value)` - find an exact match of the `key` field with the `value`
- `search(key, value)` - begin a search of the `key` field, and return all items that contain part of the `value`
- `get_random_item()` - returns one random item from the database

Note that there aren't any write operations (as of now), but they could easily be added if needed. The operations listed above are used in [Chapter 4](https://github.com/tataraba/simplesite/blob/main/docs/04_Chapter_4.md).

### Getting Ready

First things first. Install the TinyDB library from PyPI.

```
python -m pip install tinydb
```

> Note: Obligatory reminder that you only need to install if you're following along from scratch.

In your project root, create a new directory called `data`. This is where your TinyDB database file will live.

Add `DATA_DIR` to your config file and point it to this new `data` directory.

Create `crud.py` within your `app` directory, which will contain the basic helper class listed above.

Lastly, we need some data to use in the next chapter. If you want to follow along, it's best to use the data in this repo. Note tha TinyDB uses `JSON` as its storage type.

Copy the `data.json` file to your local environment. The file contains two "tables" ("artist_info" and "artist_details") which I'll reference later.

If you have experience creating your own ORM/ODM layer and want to work with your own data, you can choose to do that as well, but you'll have to follow in parallel in the next chapter.

> Note: I totally recommend using your own database layer if you're comfortable with it! The idea remains the same. Make a database call, return the objects back to the template. For example, if your database call returns a Pydantic model, you can pass that object to the template, and then access the value of the model attributes from within the template.

### Data

If you do choose to use the data I've supplied&mdash;it contains a sampling of some of the artists that tend to make the rounds on my playlists (don't judge).

The data was gathered from the [Discogs API](https://www.discogs.com/developers/). Discogs is an online database and marketplace of music releases&mdash;mostly geared toward collectors. Although I'm not a collector myself, I am grateful for their open API where I can get info on some of my favorite artists.

Elsewhere, I built a small API app to gather some resources for me. I used a [small Python library](https://python3-discogs-client.readthedocs.io/en/latest/index.html) called `python3-discogs-client` to make requests from the Discogs API.

Conducting an artist search from the the `discogs_client` provides a set of data which includes the artist's ID number (useful for gathering more details from the Discogs API), a url to an image, and other basic information.

The results of that search are in the "artist_info" table.

The second table contains the result of the data returned by the Discogs API when requesting artist information based on their ID. The [Discogs documentation has an example](https://www.discogs.com/developers/#page:database,header:database-artist) of what the response looks like.

This table is called "artist_details".

It contains more information on the artists, including a small profile/bio (in most cases), active (and inactive) members, as well as a list of different images associated with the artist.

Both of these datasets are used in the examples.

### CRUD

Feel free to use TinyDB directly if you feel comfortable doing so. Otherwise, copy the code in `crud.py` into your own application.

Here's how you use the class.

To instantiate the database, you can create one like this:

```
db = CRUD()
```

However, the data in `data.json` is contained within two tables that you have to instantiate explicitly. To do so, you can use the `classmethod` as part of the assignment.

```
db = CRUD().with_table("artist_info")
```

Now, all the operations will be done against the "artist_info" table contained in `data.json`.

To search for all artists with a name that contains the string "the" as part of their name:

```
artists = db.search(key="name", value="the")
```

The `artists` object will be a `list` of `dict` items matching the query.

### Request -> Database -> Response -> Template

Now it's time to put the pieces together. So here's the plan.

When a user visits our home page, we want to show them an image of a random artist, along with their name underneath the image.

Our little **Simple Site** will now transform into something like a digital CD Binder.

So let's follow the request at each step of the way.

When a user visits your homepage, they are sending a request. We've already built a route/view for this request in `routes.py`.

```py
@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
```

Now, when that request is made, let's make a call to the database and get a random item from our "artist_info" table. Insert this bit into your `index` method:

```py
db = CRUD().with_table("artist_info")
random_artist = db.get_random_item()
```

Now that you have a `dict` object called `random_artist`, you can send it to your template in the template "context".

```py
return templates.TemplateResponse(
      "main.html",
      {
          "request": request,
          "random_artist": random_artist,
      }
  )
```

> Note: The "context" contains a key item called `random_artist`, and the assigned value is the object `random_artist`. These **do not** have to match. For example, you could use {"artist": random_artist} instead. This just means that you would access the `random_artist` object within your template with the value assigned to the key (i.e., `artist`). I ordinarily match the key:value strings so as to prevent confusion.

Now, let's go back to `main.html` in your `templates` directory. You can now use `{{ random_artist }}` to access the `dict` item obtained from the `db.get_random_item()` database call.

Update your `main.html` file to match the following:

```html
{% extends "/shared/_base.html" %}

{% block content %}
    <section id="body" class="flex flex-col bg-slate-50 justify-center items-center max-w-screen-lg m-auto">
        <div class="flex flex-col justify-center items-center py-10">
            <h2 class="text-2xl leading-relaxed text-slate-800 uppercase">Welcome</h2>
            <div class="flex flex-col justify-center content-center text-center">
                <img src="{{random_artist['cover_image']}}" />
                <span class="py-4 uppercase font-bold">{{random_artist["name"]}}</span>
            </div>
        </div>
    </section>
{% endblock %}
```

Notice that we are accessing the `random_artist` object within our `{{ ... }}` expression.

Since the object is a `dict`, we can access values the same way we are used to in Python. In other words, the `{{random_artist['cover_image']}}` will return the _value_ of the `cover_image` key in the `random_artist` dictionary!

I'll have you guess what `{{random_artist['name']}}` will get you. :sunglasses:

Notice tha the above code contains a lot of markup within the HTML elements. If you've been playing around with TailwindCSS, you should be able to guess what's happening there.

Either way, I would encourage you to take change some of those values, and other elements as you see fit, and make it your own!

### Extras

Once you are comfortable with the cycle of request->database->response->template, start branching out and creating other routes.

This might mean creating new templates as well.

You may also think about creating a navigation header which includes links to other parts of your application. If you want this navigation bar to persist throughout your app, you only need to create it once.

For example, create a new file in your `templates/shared` directory and call it `_header.html`. In this file, create a basic navigation element (it can look something like this&mdash;hopefully the `<div>`s aren't too intimidating):

```html
<header class="bg-zinc-400 text-slate-900">
    <div class="mx-auto flex flex-col justify-between h-full items-center p">
        <nav class="flex flex-row self-start w-full h-28 py-2">
            <div id="links" class="flex flex-row items-center uppercase">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/catalog">Links</a>
            </div>
        </nav>
    </div>
</header>
```

Note that there are no Jinja markers on this file. That is because you want to _include_ this markup in your _base_ html file.

You can do that by adding this to your `_base.html` file:

```html
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"/>
  <title>{{ page_title }}</title>
  <meta name="description" content="{{ page_description }}"/>
</head>
<body>

    {% block header %}
    {% include "/shared/_header.html" %}
    {% endblock %}

    {% block content %}
    <h1>Hello, there!</h1>
    {% endblock %}
</body>
</html>
```

Now, any time your `_base.html` is included in other templates (i.e., `main.py`), it will also render the content within the `{% block header %}`. Any changes you make to your navigation file will then propagate to all your pages!

Use the same logic to add a persistent "footer" on all your pages.

For extra extra credit, create a new template that generates a page with the name of all the artists in the "artist_details" database table.

Even better if you can include the _active_ members associated with the artist record.

For reference, the `json` database record for a particular artist might look like this:

```json
{
    "data_quality": "Needs Major Changes",
    "id": 2484044,
    "images": [
        {
            "height": 528,
            "resource_url": "https://i.discogs.com/ZLKgUB45KsW5o2aBnbtDh_s6IfJbcVnFMU9_EeU7Dho/rs:fit/g:sm/q:90/h:528/w:500/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTI0ODQw/NDQtMTQ5Mjk5NDcy/MS01NjI1LmpwZWc.jpeg",
            "type": "primary",
            "uri": "https://i.discogs.com/ZLKgUB45KsW5o2aBnbtDh_s6IfJbcVnFMU9_EeU7Dho/rs:fit/g:sm/q:90/h:528/w:500/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTI0ODQw/NDQtMTQ5Mjk5NDcy/MS01NjI1LmpwZWc.jpeg",
            "uri150": "https://i.discogs.com/PhsJDVejG5aB8kgdGcEW-Nxcth_SaFpDy9klYYFx_pg/rs:fit/g:sm/q:40/h:150/w:150/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTI0ODQw/NDQtMTQ5Mjk5NDcy/MS01NjI1LmpwZWc.jpeg",
            "width": 500
        }
    ],
    "members": [
        {
            "active": true,
            "id": 1820198,
            "name": "Jay Clifford",
            "resource_url": "https://api.discogs.com/artists/1820198",
            "thumbnail_url": ""
        },
        {
            "active": true,
            "id": 2484047,
            "name": "Evan Bivins",
            "resource_url": "https://api.discogs.com/artists/2484047",
            "thumbnail_url": ""
        },
        {
            "active": true,
            "id": 2959336,
            "name": "Ward Williams (2)",
            "resource_url": "https://api.discogs.com/artists/2959336",
            "thumbnail_url": "https://i.discogs.com/YJqSBaPrIiMrN06zQ3zEOgAyz3DldNhmmXveQWnVqkw/rs:fit/g:sm/q:40/h:334/w:500/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTI5NTkz/MzYtMTU4OTM5Nzcz/Ni02MTA0LmpwZWc.jpeg"
        },
        {
            "active": true,
            "id": 5674068,
            "name": "Matthew Bivins",
            "resource_url": "https://api.discogs.com/artists/5674068",
            "thumbnail_url": ""
        }
    ],
    "name": "Jump, Little Children",
    "namevariations": [
        "Jump",
        "Jump Little Children"
    ],
    "profile": "",
    "releases_url": "https://api.discogs.com/artists/2484044/releases",
    "resource_url": "https://api.discogs.com/artists/2484044",
    "uri": "https://www.discogs.com/artist/2484044-Jump-Little-Children"
}
```

The key is getting all database items from the "artist_details" table and sending the result (a `list` of `dict` items) to your template.

In the template, you can loop over the list, each time generating everything within the loop.

For example:

```html
{% for artist in artists %}
<div class="flex flex-col bg-slate-200 content-center text-center h-12">
    <span>{{artist["name"]}}</span>
</div>
{% endfor %}
```

If `artists` is a `list` of `dict` items, this will iterate over the list and each time, render a `<div>` element with the artist's name rendered within it.

> Note: You don't always have to send the database response directly to the template. A lot of times, you may want to do some processing within the FastAPI method before returning anything to the template. Look at the `routes.py` file in the repo, and notice the specific route for the catalog page. There are functions defined within this route that are then passed directly to the template!


Once you're comfortable with this server-side web app, you may be ready to add some 🎇pizzaz🎇. If that's you, then you're ready to move to [Chapter 4](https://github.com/tataraba/simplesite/blob/main/docs/04_Chapter_4.md).
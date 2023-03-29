# :sparkles:Build a Python-Backed Frontend With HTMX and TailwindCSS:sparkles:

### Table of Contents
| Branch | Chapter | Title
| --- | --- | --- |
| Preface | [Getting Started](https://github.com/tataraba/simplesite/blob/main/docs/00_Preface.md) | [`main`](https://github.com/tataraba/simplesite) |
| Chapter 1 | [Using Jinja Templates to Render HTML](https://github.com/tataraba/simplesite/blob/main/docs/01_Chapter_1.md) | [`01_templates`](https://github.com/tataraba/simplesite/tree/01_templates) |
| Chapter 2 | [Harnessing TailwindCSS for Consistent Design](https://github.com/tataraba/simplesite/blob/main/docs/02_Chapter_2.md) | [`02_tailwindcss`](https://github.com/tataraba/simplesite/tree/02_tailwindcss) |
| Chapter 3 | [A Thin Database Layer](https://github.com/tataraba/simplesite/blob/main/docs/03_Chapter_3.md) | [`03_tinydb`](https://github.com/tataraba/simplesite/tree/03_tinydb) |
| Chapter 4 | [Modern Browser Features Directly from HTML](https://github.com/tataraba/simplesite/blob/main/docs/04_Chapter_4.md) | [`04_htmx`](https://github.com/tataraba/simplesite/tree/04_htmx)  |

## 📚 Chapter 4: Modern Browser Features Directly from HTML

If you're here, you're either curious about htmx and what it can do, or ready to ditch unneeded complexity in your web stack. You may have even heard that it can eliminate your need to learn JavaScript!

Is this true?

The answer is...

Mostly? Maybe? Yes?

For a real world case, I would look no further than this DjangoCon EU 2022 talk, titled [From React to htmx on a real-world SaaS product: we did it, and it's awesome!](https://youtube.com/watch?v=3GObi93tjZI&si=EnSIkaIECMiOmarE)

I'm not going to reiterate everything contained in the video, but I think it makes a compelling case that it's not only _possible_ to build without a JavaScript front end, but in many ways, it is _beneficial_!

Just in case, though, I do want to address some common questions that may come up when considering an htmx-centric approach.

What are some of the tradeoffs when using this type of "multi-page application" (MPA) versus a JavaScript driven "single-page application" (SPA)?

There is an [excellent essay over at htmx.org](https://htmx.org/essays/a-response-to-rich-harris/) which talks about this in detail, but here are a few key points:

- On having to load content on every request: If you're having consistent calls on every request, you could cache that content. But for the most part, with htmx, requests are generally light-weight replacements of Document Object Model (DOM) elements. (How web pages are represented internally to a browser.)
- On network latency issues: an MPA may suffer if the server is experiencing latency. However, with optimizations like database tuning, Redis caching, and so on, quick responses are easily achievable. The problem with latency is that it makes an app feel laggy&mdash;and this is not really a solved problem in the JavaScript world.
- On ✨ pizzaz ✨: Transitions and animations are much nicer with JavaScript. However, adding these elements doesn't mean much in terms of long-term accessibility and usability concerns. In any respect, using clever CSS design, as well as with the htmx support for standard CSS transitions, a lot of that sparkle can be replicated.

Okay with all that out of the way, let's get to it.

### Installing?

There's a question mark there because you don't actually _have_ to install anything. Htmx is a dependency-free, browser-oriented JavaScript library. Using it is as straightforward as adding it to a `<script>` tag in your HTML document head.

To test it out, you could just use a CDN. To do so, add this line within your document head:

```html
<script src="https://unpkg.com/htmx.org@1.8.6" integrity="sha384-Bj8qm/6B+71E6FQSySofJOUjA/gq330vEqjFx9LakWybUySyI1IQHwPtbTU7bNwx" crossorigin="anonymous"></script>
```

But perhaps the next easiest way (and what I recommend) is to copy it into your project.

Within your `static` directory, create a new folder and call it `js`. You can get the file from [unpkg.com](https://unpkg.com/htmx.org@1.8.6/dist/htmx.min.js). Either download it, or copy the contents and create a file in your `js` directory. (I've called my file `htmx.min.js`). (Or, you could use the same file in this template.)

Now, add the script element to your document head. You can use the Jinja `url_for()` method to access it, since it is contained within your static directory.

```html
<script src="{{ url_for('static', path='js/htmx.min.js') }}"></script>
```

And that's it!

### The Python Stuff

You actually don't _need_ any additional Python packaging to use htmx.

There is one library, however, that I use in order to ease the building of templates. I'll get into that later, but for now, let's go ahead and install it.

```
python -m pip install jinja2-fragments
```
> Note: Okay, you should already know by now...

This creates a drop-in replacement for the FastAPI `Jinja2Templates` object. To use it, use `Jinja2Blocks` instead.

Open your `routes.py` file and make the substitution noted above. The top of your module will look something like this:

```py
from fastapi import APIRouter, Request
from jinja2_fragments.fastapi import Jinja2Blocks

from app.config import Settings

templates = Jinja2Blocks(directory="path/to/templates")
```

This will enable you to render "template fragments." (You can [read more about this paradigm](https://htmx.org/essays/template-fragments/) on the htmx.org website).

Without getting into the details (yet), this means that a `TemplateResponse` can find a defined section _within_ an existing template file, and only send that content over to the DOM.

But before delving into that, let's find out how to actually use htmx!

### Using htmx

At the core, htmx contains a set of attributes that allow you to issue AJAX requests directly within your HTML.

Here are a few of those:

- `hx-get` - issues `GET` request to given URL
- `hx-post` - issues `POST` request to given URL
- `hx-delete` - issues `DELETE` request to given URL

(Same applies for `PUT` and `PATCH`)

While these events are triggered by the "natural" event of an element (usually a "click" event), htmx also allows you to define which behavior will trigger the AJAX request. These are defined with an `hx-trigger` attribute. (i.e., mouseover, keypress, etc...)

And very importantly, you can also define the element where the response will be loaded. By default, the response will be loaded into the element that triggered the AJAX request.

But if you want the response to be loaded elsewhere, you can use the `hx-target` attribute to specify which element should receive the response (this attributes takes a CSS selector as its value).

This makes more sense with an example (taken from [htmx.org](https://htmx.org/docs/)):

```html
<button hx-post="/clicked"
    hx-trigger="click"
    hx-target="#parent-div"
    hx-swap="outerHTML"
>
    Click Me!
</button>
```

When a user clicks (`hx-trigger`) on this button, a `POST` request is sent to the "/clicked" endpoint (`hx-post`). The response will be sent back looking for an element with the CSS `id` "#parent-div" (`hx-target`), and the entire element will be replaced (`hx-swap`).

As you can see, htmx is very declarative with its intentions!

One of the attributes introduced above is `hx-swap`. This defines how the response is swapped into the existing DOM.

A few examples:

- "innerHTML" - the default, puts the content inside the target element
- "outerHTML" - replaces the entire target element with the returned content
- "afterbegin" - prepends the content before the first child inside the target
- "afterend" - appends the content after the target in the targets parent element

### Request Headers

There are times where a request is made to a specific route/view/endpoint, but the response should vary based on whether it's a "regular" request, or one coming from htmx.

For example, a regular request expects the entire web page to refresh. However, an `hx-get` request only expects a response specific to the element being replaced.

In order for your web app to understand what kind of request it is receiving, htmx sends data within the Request Header.

FastAPI has access to this request object, and you can parse it in order to obtain specific Header information.

**All htmx requests will send an HX-Request header with its value set to `true`.**

This is extremely important, as you are able to write logic within your route/view/endpoint to handle that kind of request.

Additionally, htmx also sends relevant data through other Headers. Two important ones are:
- `HX-Target` - the `id` of the target element if it exists
- `HX-Trigger` - the `id` of the triggered element if it exists
- `HX-Current-URL` - the current URL of the browser

There are more, but these will suffice for now.

### Using With FastAPI

Let's take a look at how an htmx request might be handled in your app:

```py
@router.get("/page")
def some_page(request: Request):

    template = "full_content.html"

    if request.headers.get("HX-Request"):
        template = "partial_content.html"

    return template.TemplateResponse(
        template,
        {
            "request": request,
        }
    )
```

Since we've learned that `HX-Request` is a boolean, the conditional checks to see if it can be retrieved from the Request Headers. If so, the name of the template changes from `full_content.html` to `partial_content.html`.

Then, the `TemplateResponse` sends the corresponding response based on how the request was made.

### Let's Try It Out

You can also use the same pattern above to differentiate what gets sent through the template context, or to isolate what kind of database call should be made. Either way, you have full control of what gets sent back to the client.

It's now time to put it all together.

In the `routes.py` file, create an endpoint for `/catalog`.

When a user navigates to this endpoint, we want to give show cards of all the artists that are in the "artist_details" table of TinyDB.

Make a call to the database that gets all artist data, and send that data to your template.

In your template, you can iterate over that list of artists and extract the artist name.

Create `<div>` elements using Tailwind to resemble square or rectangular "cards".

Using Jinja, iterate over the artist data sent to the template in order to display a `<div>` element for each artist in the database.

Once you have that part working, create an htmx request on the `<div>` element that displays the artist card.

The htmx request should obtain the artist profile (it should be contained within the same `dict` object used for artist name).

And for extra credit, make it so that when you click the card again, it returns to the artist name.

### Active Search

For the final exercise...

- will need to install python-multipart to receive form data (search)
  - python -m pip install python-multipart
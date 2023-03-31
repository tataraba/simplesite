from typing import Annotated

from fastapi import APIRouter, Form, Request
from jinja2_fragments.fastapi import Jinja2Blocks
from pydantic import BaseModel

from app.config import Settings
from app.crud import CRUD

settings = Settings()
templates = Jinja2Blocks(directory=settings.TEMPLATE_DIR)

router = APIRouter()

class Search(BaseModel):
    search: str | None = None

@router.get("/")
def index(request: Request):
    """Home page - generates an image and name of a random artist."""

    db = CRUD().with_table("artist_info")
    random_artist = db.get_random_item()

    return templates.TemplateResponse(
            "main.html",
            {
                "request": request,
                "artist_count": len(db.all_items()),
                "random_artist": random_artist,
            }
        )


@router.get("/about")
def about(request: Request):
    """About page - some background information about this app."""

    return templates.TemplateResponse("about.html", {"request": request})


@router.get("/catalog")
def catalog(request: Request):
    """Catalog page - display information about artists in database."""

    db = CRUD().with_table("artist_details")
    artists = db.all_items()

    def get_members(artist: dict):
        """This returns active members from the artist_details table. This
        method can be used within the Jinja template."""

        if "members" not in artist:
            return [artist["name"]]
        all_members = artist["members"]
        active_members = []
        for member in all_members:
            if member["active"]:
                active_members.append(member["name"])
        return active_members # limit 14 members

    def get_website(artist: dict):
        if "urls" not in artist:
            return artist["uri"]  # send discogs uri if no url found
        return artist["urls"][0]

    def get_profile(artist: dict):
        if not artist["profile"]:
            return "No profile available"
        else:
            profile = artist["profile"]
            profile = profile.replace("[", "<").replace("]", ">")
            return profile

    if request.headers.get("hx-request"):
        id = request.headers.get("HX-Trigger")
        artist = db.find("id", int(id))
        print(artist)
        return templates.TemplateResponse(
            "artist/profile.html",
            {
                "request": request,
                "artist": artist[0],
                "get_website": get_website,
                "get_profile": get_profile,
            }
        )

    return templates.TemplateResponse(
            "catalog.html",
            {
                "request": request,
                "artists": artists,
                "get_members": get_members,
                "get_website": get_website,
            }
        )

@router.get("/profile")
def profile(request: Request):
    """Profile page - display information about a specific artist."""

    # db = CRUD().with_table("artist_details")


    if request.headers.get("hx-request"):
        pass


@router.get("/search")
def search(request: Request):
    """Search page - display information about artists in database."""
    block_name = None
    if request.headers.get("hx-request"):
        block_name = "content"
    results = []

    return templates.TemplateResponse(
        "search.html",
        {
            "request": request,
            "results": results
        },
        block_name=block_name
    )




@router.post("/search")
def search_post(request: Request, search: Annotated[str, Form()]):

    print(search)
    block_name = None
    if request.headers.get("hx-request"):
        block_name = "artist_card"

    db = CRUD().with_table("artist_details")
    # block_name = "artist_card"
    results=[]
    artists = db.search(key="name", value=search)
    print(artists)
    def get_members(artist: dict):
        """This returns active members from the artist_details table. This
        method can be used within the Jinja template."""

        if "members" not in artist:
            return [artist["name"]]
        all_members = artist["members"]
        active_members = []
        for member in all_members:
            if member["active"]:
                active_members.append(member["name"])
        return active_members # limit 14 members

    def get_website(artist: dict):
        if "urls" not in artist:
            return artist["uri"]  # send discogs uri if no url found
        return artist["urls"][0]

    return templates.TemplateResponse(
        "catalog.html",
        {
            "request": request,
            "results": results,
            "artists": artists,
            "get_website": get_website,
            "get_members": get_members,

        },
        block_name=block_name
    )

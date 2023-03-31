from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.config import Settings
from app.crud import CRUD

settings = Settings()
templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)

router = APIRouter()


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

    return templates.TemplateResponse(
            "catalog.html",
            {
                "request": request,
                "artists": artists,
                "get_members": get_members,
                "get_website": get_website,
            }
        )

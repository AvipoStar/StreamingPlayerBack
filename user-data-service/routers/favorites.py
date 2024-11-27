from fastapi import APIRouter

from controllers.favorites import addTrack, removeTrack

router = APIRouter()


@router.post('/', tags=["Favorites"])
def add_to_favorites(track_id: int):
    result = addTrack(track_id)
    return result


@router.delete('/', tags=["Favorites"])
def remove_from_favorites(track_id: int):
    result = removeTrack(track_id)
    return result

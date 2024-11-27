from fastapi import APIRouter

from controllers.playlist import createPlaylist, addTrack, removeTrack, deletePlaylist, changeName
from models.playlist import Playlist, TrackPlaylist

router = APIRouter()


@router.post('/', tags=["Playlist"])
def create_playlist_endpoint(playlist: createPlaylist):
    playlist_id = createPlaylist(playlist)
    return {"playlist_id": playlist_id}


@router.delete('/', tags=["Playlist"])
def delete_playlist_endpoint(playlist_id: int):
    result = deletePlaylist(playlist_id)
    return result


@router.put('/', tags=["Playlist"])
def update_playlist_endpoint(playlist: createPlaylist):
    result = changeName(playlist)
    return result


@router.post('/track', tags=["Playlist"])
def add_track_endpoint(data: TrackPlaylist):
    result = addTrack(data.track_id, data.playlist_id)
    return result


@router.delete('/track', tags=["Playlist"])
def remove_track_endpoint(data: TrackPlaylist):
    result = removeTrack(data.track_id, data.playlist_id)
    return result

#!/bin/python3
"""
Post-processing for newly-downloaded playlists.
"""
from dataclasses import dataclass
import os


_DEFAULT_DOWNLOADS_DIR = "download"
_DEFAULT_PLAYLISTS_DIR = os.path.join(_DEFAULT_DOWNLOADS_DIR, "Playlist")


@dataclass
class Song:
    name: str
    path: str
    tags: list[str]

    def add_tag(self, tag: str):
        """Add a tag to a song."""
        if tag not in self.tags:
            self.tags.append(tag)

class Playlist(object):
    def __init__(
            self,
            name: str,
            path: str,
            tracklist: list[Song] = []
        ):
        self.name = name
        self.path = path
        self.tracklist = tracklist if tracklist else self._load_tracklist()

    def _load_tracklist(self) -> list[Song]:
        """Load all tracks from path."""
        return []


def find_playlists(base_path: str = _DEFAULT_PLAYLISTS_DIR) -> list[Playlist]:
    """Return downloaded Playlists."""
    playlists = []
    for _, dirs, files in os.walk(base_path):
        print(files)
        for playlist_path in dirs:
            print(playlist_path)
    return playlists

def altaria():
    """Post-processing steps for music downloaded from tidal-dl."""
    playlists = find_playlists()

if __name__ == "__main__":
    altaria()

#!/bin/python3
"""
Post-processing for newly-downloaded playlists.
"""
import argparse
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
            path: str,
            name: str = "",
            tracklist: list[Song] = []
        ):
        self.path = path

        self.name = (name
                     if name
                     else path.split("/")[-1])
        print(self.name)
        #self.tracklist = tracklist if tracklist else self._load_tracklist()

    def _load_tracklist(self) -> list[Song]:
        """Load all tracks from path."""
        return []


def find_playlists(base_path: str = _DEFAULT_PLAYLISTS_DIR) -> list[Playlist]:
    """Return downloaded Playlists."""
    playlists = []
    for root, dirs, files in os.walk(base_path):
        for _dir in dirs:
            if _dir:
                print(_dir)
        for file in files:
            pass
    return playlists

def altaria(base_path: str):
    """Post-processing steps for music downloaded from tidal-dl."""
    playlists = (find_playlists(base_path=base_path)
                 if base_path
                 else find_playlists())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Post-processing for downloaded music."
        )
    parser.add_argument(
            "-d",
            "--dir",
            type=str,
            default="",
            help="Path to parent directory of music."
        )
    args = parser.parse_args()
    altaria(base_path=args.dir)

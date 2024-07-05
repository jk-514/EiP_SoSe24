from __future__ import annotations
from typing import Optional


class Song:
    def __init__(self, title: str, artist: str, length: int) -> None:
        self.title: str = title
        self.artist: str = artist
        self.length: int = length

    def __str__(self) -> str:
        return f"Song({self.title}, {self.artist}, {self.length})"


class Entry:
    def __init__(self, song: Song) -> None:
        self.song: Song = song
        self.next_song: Optional[Entry] = None

    def get_next(self) -> Optional[Entry]:
        return self.next_song

    def set_next(self, next_entry: Entry) -> None:
        self.next_song = next_entry

    def __str__(self) -> str:
        return f"Entry({str(self.song)})"


class Playlist:
    def __init__(self, first_song: Song) -> None:
        self.first_song = Entry(first_song)

    def add_front(self, song: Song) -> None:
        new_entry = Entry(song)
        new_entry.set_next(self.first_song)
        self.first_song = new_entry

    def __str__(self) -> str:
        out: str = "Playlist:\n" + str(self.first_song) + "\n"

        current = self.first_song
        while (next_song := current.get_next()) is not None:
            out += str(next_song) + "\n"
            current = next_song

        return out

    def add_back(self, song: Song) -> None:
        current = self.first_song
        while (next_song := current.get_next()) is not None:
            current = next_song

        current.set_next(Entry(song))

    def __getitem__(self, index):
        current = self.first_song
        for i in range(index):
            current = current.get_next()
            if current is None:
                raise IndexError("Index out of range")
        return current.song

    def add_at(self, song, index) -> None:
        current = self.first_song
        for i in range(index-1):
            current = current.get_next()
            if current is None:
                raise IndexError("Index out of range")
        new_entry = Entry(song)
        new_entry.set_next(current.get_next())
        current.set_next(new_entry)


def generate_song_list(file_name):
    out = []
    with open(file_name) as file:
        for line in file:
            artist, title, l = line.strip().split(" - ")
            s = l.split(":")
            length = int(s[0]) * 60 + int(s[1])
            out.append(Song(title, artist, int(length)))
    return out


def main():
    songs = generate_song_list("playlist.txt")
    playlist = Playlist(songs[0])
    for song in songs[1:]:
        playlist.add_front(song)
    print(playlist)
    print()
    print(playlist[2])
    print()
    playlist.add_at(Song("New Song", "New Artist", 120), 2)
    print()
    print(playlist)


if __name__ == '__main__':
    main()

class Song:
    count = 0
    genres = []         # unique list of genres (preserve insertion order)
    artists = []        # unique list of artists (preserve insertion order)
    genre_count = {}    # maps genre -> number of songs in that genre
    artist_count = {}   # maps artist -> number of songs by that artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # increment global song count
        Song.add_song_to_count()

        # ensure unique lists and update counts
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add genre to the unique genres list (no duplicates)."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add artist to the unique artists list (no duplicates)."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the count of songs for this genre."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increment the count of songs for this artist."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

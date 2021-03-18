class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        [self.photos.append([]) for _ in range(self.pages)]
        self.count_slots = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(int(photos_count / 4))

    def add_photo(self, label: str):
        count = 0
        for page in self.photos:
            count += 1
            if len(page) < 4:
                page.append(label)
                self.count_slots += 1
                if self.count_slots > 4:
                    self.count_slots = 1
                return f"{label} photo added successfully on page {count} slot {self.count_slots}"
        return "No more free spots"

    def display(self):
        result = ''
        for row in self.photos:
            result += f'{"-" * 11}\n'
            if len(row) > 0:
                result += f'{" ".join(["[]" for el in row])}\n'
            else:
                result += '\n'
        result += f'{"-" * 11}\n'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


import os
import exif
from exif import Image

# for value in sorted(image.list_all()):
#     print(f'{value}: {type(image.get(value))}')
#     image.gps_latitude = (0.0, 0.0, 0.0)
#     print(f'{value}: {image.get(value)}')

def change_metadata(f):
    with open(f, 'rb') as file:
        image = Image(file)

    old_data = image.gps_latitude + image.gps_longitude
    image.gps_latitude = (0.0, 0.0, 0.0)
    image.gps_longitude = (0.0, 0.0, 0.0)
    
    with open(f, 'wb') as file:
        file.write(image.get_file())

    return f'{f} metadata was changed {old_data} -> {image.gps_latitude + image.gps_longitude}'


with os.scandir('.') as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file() and not entry.name.endswith('.py'):
            print(f'Working on {entry.name}' + change_metadata(entry.name))
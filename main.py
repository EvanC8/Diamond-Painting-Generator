from PIL import Image

from HelperCode.ImageEffects import pixelate

# import desired image python file
from PaintingsData.StarryNight import starry_night

# select python file to produce diamond painting from
selected_image = starry_night

square_length = selected_image.square_length

# access image and crop it to perfectly fit desired pixel chunk size
input_image = Image.open(selected_image.image)

init_width, init_height = input_image.size

width = init_width - (init_width % square_length)
height = init_height - (init_height % square_length)

input_image = input_image.crop((0, 0, width, height))

# increase abstraction of image by grouping pixels into pixel chunks and reducing image size
pixel_map = pixelate(input_image, square_length, width, height)

# quantize pixel_map image; Use palette if provided
if selected_image.palette is not None:
    palette_data = selected_image.palette

    NUM_ENTRIES_IN_PILLOW_PALETTE = 24#256
    num_bands = len("RGB")
    num_entries = len(palette_data) // num_bands
    palette_data.extend(palette_data[:num_bands] * (NUM_ENTRIES_IN_PILLOW_PALETTE - num_entries))

    arbitrary_size = 6, 4
    pal_image = Image.new('P', arbitrary_size)
    pal_image.putpalette(palette_data)

    pixel_map = pixel_map.quantize(palette=pal_image)
else:
    pixel_map = pixel_map.quantize(colors=selected_image.colorCount, method=2, dither=Image.Dither.RASTERIZE)

# re-size image to original size
pixel_map = pixel_map.resize((width, height))

# save diamond painting
pixel_map.save("Outputs/" + selected_image.output, format="png")

# display diamond painting
pixel_map.show()
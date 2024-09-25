from HelperCode.ImageData import ImageData

starry_night_palette = [
            35, 36, 39,
            54, 52, 50,
            50, 62, 95,
            64, 81, 119,
            29, 38, 77,
            26, 40, 115,
            42, 61, 133,
            64, 86, 148,
            75, 68, 60,
            94, 107, 127,
            89, 109, 160,
            85, 88, 92,
            240, 243, 237,
            17, 17, 21,
            212, 219, 215,
            184, 192, 194,
            154, 165, 176,
            128, 137, 140,
            115, 134, 174,
            127, 120, 99,
            226, 217, 124,
            175, 168, 112,
            117, 92, 55,
            212, 153, 40,
        ]

starry_night = ImageData(
    image="images/image2.jpg", # image file location
    square_length=10, # desired pixel chunk size
    palette=starry_night_palette, # desired color palette for quantization or None
    color_count=24, # number of colors in palette or desired number of colors for quantization
    output="StarryNight" # name for output image file
)
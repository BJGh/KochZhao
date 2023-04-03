from PIL import Image

# function to convert a character to its binary representation
def charToBinary(char):
    binary = bin(ord(char))[2:]
    return '00000000'[len(binary):] + binary
  
# function to hide a message in an image
def hideImage(source_image_path, message_image_path, output_image_path):
    # Open the source image and message image
    source_image = Image.open(source_image_path)
    message_image = Image.open(message_image_path)
  
    source_pixels = source_image.load()
    message_pixels = message_image.load()

    # Resize the message image to be the same as the source image
    message_image = message_image.resize(source_image.size)

    # Create a new image to store the output pixels
    output_image = Image.new(message_image.mode, message_image.size)
    output_pixels = output_image.load()

    # Iterate over the pixels in the message image
    for i in range(message_image.size[0]):
        for j in range(message_image.size[1]):
            message_pixel = message_pixels[i, j]
            # Get the RGB values of the message pixel
            red, green, blue = message_pixel

            # Convert the RGB values to binary
            red_binary = charToBinary(chr(red))
            green_binary = charToBinary(chr(green))
            blue_binary = charToBinary(chr(blue))

            # Iterate over the binary strings and set the least significant bit of each source pixel to the corresponding bit in the message pixel
          # Iterate over the binary strings and set the least significant bit of each source pixel to the corresponding bit in the message pixel
            for k, bit in enumerate(red_binary):
                source_pixel = source_pixels[i, j]
                source_red, source_green, source_blue = source_pixel
                source_red_binary = charToBinary(chr(source_red))
                source_red_binary = source_red_binary[:-1] + bit
                source_red = int(source_red_binary, 2)
                source_pixels[i, j] = (source_red, source_green, source_blue)

            for k, bit in enumerate(green_binary):
                source_pixel = source_pixels[i, j]
                source_red, source_green, source_blue = source_pixel
                source_green_binary = charToBinary(chr(source_green))
                source_green_binary = source_green_binary[:-1] + bit
                source_green = int(source_green_binary, 2)
                source_pixels[i, j] = (source_red, source_green, source_blue)
              
            for k, bit in enumerate(blue_binary):
                source_pixel = source_pixels[i, j]
                source_red, source_green, source_blue = source_pixel
                source_blue_binary = charToBinary(chr(source_blue))
                source_blue_binary = source_blue_binary[:-1] + bit
                source_blue = int(source_blue_binary, 2)
                source_pixels[i, j] = (source_red, source_green, source_blue)

    # Save the modified source image to the output path
    source_image.save(output_image_path,'png')
hideImage('cat.jpg','qr.png','result')
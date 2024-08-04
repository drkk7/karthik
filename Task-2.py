def encrypt_image(input_image_path, output_image_path, key):
    # Load the image
    image = Image.open(input_image_path)
    pixels = image.load()
    
    # Encrypt the image by manipulating pixel values
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            # Simple encryption by adding the key
            pixels[i, j] = (r + key) % 256, (g + key) % 256, (b + key) % 256
    
    # Save the encrypted image
    image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Load the image
    image = Image.open(input_image_path)
    pixels = image.load()
    
    # Decrypt the image by reversing the pixel manipulation
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            # Reverse the encryption by subtracting the key
            pixels[i, j] = (r - key) % 256, (g - key) % 256, (b - key) % 256
    
    # Save the decrypted image
    image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

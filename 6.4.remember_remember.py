from PIL import Image

def remember_remember():
  """
  Prints secret message from image file where each position
  Of black pixel line is the ascii value of a charecter

  Returns:
      str: The secret message
  """
  
  with Image.open(r"resources\code.png").convert("RGB") as im:
    px = im.load()
  
  secret_message = ''
  for i in range(im.width):
    for j in range(im.height):
      if px[i,j] == (1,1,1):
        secret_message += chr(j)
  return secret_message
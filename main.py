import numpy as np
import cv2
from ultralytics import YOLO

model= YOLO('yolo11n-seg.pt')

def image_background_remove(image_path):
  results= model(image_path) #for image

  r= results[0]



  masks= r.masks.data.cpu().numpy()
  mask=0
  for i,value in enumerate(masks):
    mask+=masks[i]
  mask = (mask * 255).astype(np.uint8)
  # Read the original image
  img = cv2.imread(image_path) #if you send image

  # Resize mask to image size
  mask_resized = cv2.resize(mask, (img.shape[1], img.shape[0]))

  # Create 3-channel mask for RGB image
  mask_rgb = cv2.merge([mask_resized, mask_resized, mask_resized])

  # Apply mask
  result = cv2.bitwise_and(img, mask_rgb)

  # Show output with black background
  #cv2_imshow(result)

  # Add alpha channel
  b, g, r = cv2.split(result)
  rgba = cv2.merge([b, g, r, mask_resized])

  # show as PNG with transparency
  return rgba



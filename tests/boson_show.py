import cv2
import numpy as np
from bosonpy.boson import Boson

with Boson() as camera:
    while True:
        img = camera.grab().astype(np.float32)

        # Rescale to 8 bit
        img = 255*(img - img.min())/(img.max()-img.min())

        cv2.imshow('Boson', img.astype(np.uint8))
        if cv2.waitKey(1) == 27:
            break  # esc to quit
        
cv2.destroyAllWindows()
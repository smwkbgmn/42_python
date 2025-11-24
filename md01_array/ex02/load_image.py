import cv2
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path and return it as a NumPy array.

    :param path: Description
    :type path: str
    :return: Description
    :rtype: ndarray
    """
    try:
        # Load image
        image = cv2.imread(path)  # Returns a NumPy array

        # Check if image was loaded successfully
        if image is None:
            raise ValueError(f"Unable to load image from '{path}'")

        # Convert from BGR to RGB (OpenCV loads in BGR by default)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Print format and shape information
        print(f"The shape of image is: {image_rgb.shape}")

        return image_rgb

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return np.array([])

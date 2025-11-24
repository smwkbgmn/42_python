import numpy as np
import cv2
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_zoom(image: np.ndarray, zoom_size: int) -> np.ndarray:
    """Crop center portion of image.

    Args:
        image: Input image array
        zoom_size: Size of square crop

    Returns:
        Cropped image
    """

    # Get height and weidth
    h, w = image.shape[:2]

    # Calculate center crop coordinates
    len = zoom_size // 2
    center = (h // 2, w // 2)

    # Slice the image (NumPy array slicing)
    cropped = image[center[0] - len : center[0] + len,
                    center[1] - len : center[1] + len]

    # Print shape information
    print("The shape of cropped image is", cropped.shape)

    return cropped


def ft_gray(image: np.ndarray) -> np.ndarray:
    """Convert image to grayscale.

    Args:
        image: Input image array

    Returns:
        Grayscale image
    """

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # Shape: (400, 400)

    # Keep as 2D for simplicity - works with matplotlib/OpenCV
    # Use 3D (H, W, 1) only if needed for: neural networks,
    # batch processing, or consistent API with RGB
    # gray = gray[:, :, np.newaxis]  # Would make shape: (400, 400, 1)

    # Print shape information
    print("The shape of gray_scale image is", gray.shape)

    return gray


def display(image: np.ndarray, title: str = "Zoomed Image") -> None:
    """Display image with matplotlib showing axis scales.

    Args:
        image: Image array to display
        title: Window title
    """
    plt.figure(figsize=(8, 8))

    # Display grayscale image
    # cmap='gray' ensures it displays in grayscale
    plt.imshow(image, cmap='gray')

    # Add title
    plt.title(title)

    # Show axis with pixel coordinates
    plt.xlabel('X axis (pixels)')
    plt.ylabel('Y axis (pixels)')

    # Show the plot
    plt.show()


def main() -> None:
    """Main function to load, ft_, and display image."""

    WD_PATH = "/Users/donghyun/All/dev/python_data_science/md01_array/"
    IMAGE_NAME = "animal.jpeg"

    try:
        # Load the image
        print("Loading image...")
        print(image := ft_load(WD_PATH + IMAGE_NAME))

        # Zoom (crop + convert to grayscale)
        print("\nZooming image...")
        print(zoomed := ft_zoom(image, zoom_size=400))

        # Turn to gray scale image
        print("\nConverting to gray scale...")
        print(gray := ft_gray(zoomed))

        # Display with scales
        display(gray)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

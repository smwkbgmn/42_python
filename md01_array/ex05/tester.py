import matplotlib.pyplot as plt
from load_image import ft_load
import pimp_image as pimp


def main() -> None:
    """Main function to load, ft_, and display image."""

    WD_PATH = "/Users/donghyun/All/dev/python_data_science/md01_array/"
    IMAGE_NAME = "landscape.jpg"

    try:
        print(image := ft_load(WD_PATH + IMAGE_NAME))

        filters = [
            (image, "Original"),
            (pimp.ft_invert, "Inverted"),
            (pimp.ft_red, "Red"),
            (pimp.ft_green, "Green"),
            (pimp.ft_blue, "Blue"),
            (pimp.ft_grey, "Greyscale")
        ]

        # Create subplots
        _, axes = plt.subplots(2, 3, figsize=(15, 10))

        # Set the framse with image, title, and no axis
        for ax, (flt, title) in zip(axes.flat, filters):
            ax.set_title(title)
            ax.axis('off')

            # Except one case of original image, adjust filter
            if title == "Original":
                ax.imshow(image)
            else:
                ax.imshow(flt(image.copy()))
                print(flt.__doc__)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

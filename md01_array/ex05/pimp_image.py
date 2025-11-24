import numpy as np


def ft_invert(image: np.ndarray) -> np.ndarray:
    """
    Convert image as inverted

    :param image: Copied original image
    :type image: np.ndarray
    :return: Converted image
    :rtype: ndarray
    """
    # Invert value from max 255
    return 255 - image


def ft_red(image: np.ndarray) -> np.ndarray:
    """
    Convert image as being shown only red

    :param image: Copied original image
    :type image: np.ndarray
    :return: Converted image
    :rtype: ndarray
    """
    image[:, :, 1] *= 0  # Turn green value to 0
    image[:, :, 2] *= 0  # Turn blue value to 0
    return image


def ft_green(image: np.ndarray) -> np.ndarray:
    """
    Convert image as being shown only green

    :param image: Copied original image
    :type image: np.ndarray
    :return: Converted image
    :rtype: ndarray
    """
    image[:, :, 0] -= image[:, :, 0]  # Turn red value to 0
    image[:, :, 2] -= image[:, :, 2]  # Turn blue value to 0
    return image


def ft_blue(image: np.ndarray) -> np.ndarray:
    """
    Convert image as being shown only blue

    :param image: Copied original image
    :type image: np.ndarray
    :return: Converted image
    :rtype: ndarray
    """
    image[:, :, 0] = 0  # Turn red value to 0
    image[:, :, 1] = 0  # Turn green value to 0
    return image


def ft_grey(image: np.ndarray) -> np.ndarray:
    """
    Convert image as greyscale

    :param image: Copied original image
    :type image: np.ndarray
    :return: Converted image
    :rtype: ndarray
    """
    # Get grey scaled value by adding each color divied by 3
    grey_value = (
        image[:, :, 0] / 3
        + image[:, :, 1] / 3
        + image[:, :, 2] / 3
    )

    image[:, :, 0] = grey_value
    image[:, :, 1] = grey_value
    image[:, :, 2] = grey_value

    # Since divide with '/' returns float, should convert to int at last
    return image.astype(np.uint8)

from django.core.exceptions import ValidationError


def image_size_validation(mb_size, image):
    if not isinstance(mb_size, (int, float)):
        raise TypeError(f"mb_size must be an int or float, got {type(mb_size)}")
    if not hasattr(image, 'size'):
        return AttributeError('Image must have a size attribute')
    max_size = mb_size * 1024 * 1024
    if image.size > max_size:
        raise ValidationError(f"The maximum image size allowed is {mb_size}MB")


def video_size_validation(mb_size, image):
    if not isinstance(mb_size, (int, float)):
        raise TypeError(f"mb_size must be an int or float, got {type(mb_size)}")
    if not hasattr(image, 'size'):
        return AttributeError('Video must have a size attribute')
    max_size = mb_size * 1024 * 1024
    if image.size > max_size:
        raise ValidationError(f"The maximum video size allowed is {mb_size}MB")





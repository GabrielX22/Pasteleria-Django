from django.forms import ValidationError

class maximotamano:

    def __init__(self, max_file_size=10):
        self.max_file_size = max_file_size

    def __call__(self, value):
        size = value.size
        max_size = self.max_file_size * 1048576

        if size > max_size:
            raise ValidationError(f"El tamaño del archivo debe de ser de {self.max_file_size}MB")

        return value
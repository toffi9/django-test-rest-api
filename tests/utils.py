from django.core.exceptions import ValidationError

import pytest


def get_error_dict_from_model_validation(obj):
    with pytest.raises(ValidationError) as excinfo:
        obj.full_clean()
        obj.save()

    error_dict = excinfo.value.__dict__['error_dict']

    return error_dict

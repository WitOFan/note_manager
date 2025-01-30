def validate_status(status):
    if (status.lower() == 'новая') or (status.lower() == 'в процессе') or (status.lower() == 'выполнена'):
        return True
    else:
        return False
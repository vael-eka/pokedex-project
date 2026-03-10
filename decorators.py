def shout(original_func):
        def wrapper(*args, **kwargs):
            result = original_func(*args, **kwargs)

            if isinstance(result, str):
                return result.upper()
            return result
        return wrapper
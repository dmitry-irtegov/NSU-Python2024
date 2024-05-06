def cache(func):
    if not hasattr(cache, "__cache"):
        cache.__cache = {}
    return func
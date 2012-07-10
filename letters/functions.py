
def add_to_middleware(MIDDLEWARE_CLASSES_old, middleware, prepend=False):
    if middleware not in MIDDLEWARE_CLASSES_old:
        if prepend:
            return (middleware,) + MIDDLEWARE_CLASSES_old
        else:
            return MIDDLEWARE_CLASSES_old + (middleware,)
    else:
        return MIDDLEWARE_CLASSES_old

import os


def app_make_dirs():
    try:
        os.makedirs(os.path.join('application/instance'))
    except OSError:
        pass

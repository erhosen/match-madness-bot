import select
import sys
import time
from functools import wraps

from PIL import Image
from pathlib import Path


CUR_DIR = Path(__file__).parent
PROJECT_DIR = CUR_DIR.parent
IMAGES_DIR = PROJECT_DIR / "data" / "images"


class TimeoutExpired(Exception):
    pass


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print("func:%r args:[%r, %r] took: %2.4f sec" % (f.__name__, args, kw, te - ts))
        return result

    return wrap


def input_with_timeout(prompt, timeout):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    if ready:
        return sys.stdin.readline().rstrip("\n")  # expect stdin to be line-buffered

    raise TimeoutExpired


def open_image(name: str) -> Image.Image:
    return Image.open(IMAGES_DIR / name)

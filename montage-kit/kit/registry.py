"""يجمع كل الإصدارات في قوائم موحدة. العناصر الجديدة مسجلة في NEW."""
from .effects import FX
from .sfx import SFX
from .luts import LUTS
from .overlays import OVERLAYS

NEW = {"fx": set(), "sfx": set(), "luts": set(), "overlays": set(), "transitions": set()}


def _merge(target, extra, key):
    target.update(extra)
    NEW[key].update(extra)


try:
    from .effects2 import FX2
    _merge(FX, FX2, "fx")
except ImportError:
    pass
try:
    from .sfx2 import SFX2
    _merge(SFX, SFX2, "sfx")
except ImportError:
    pass
try:
    from .luts2 import LUTS2
    _merge(LUTS, LUTS2, "luts")
except ImportError:
    pass
try:
    from .overlays2 import OVERLAYS2
    _merge(OVERLAYS, OVERLAYS2, "overlays")
except ImportError:
    pass
try:
    from .transitions import TRANS, BASIC
    NEW["transitions"].update(set(TRANS) - BASIC)
except ImportError:
    TRANS = {}

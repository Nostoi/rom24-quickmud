from .area_loader import load_area_file
from pathlib import Path

from mud.registry import area_registry


def load_all_areas(list_path: str = "area/area.lst"):
    with open(list_path, 'r', encoding='latin-1') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line == '$':
                break
            path = Path('area') / line
            load_area_file(str(path))

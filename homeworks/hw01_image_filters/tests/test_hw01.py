import numpy as np
from pathlib import Path

def test_repo_layout():
    assert Path('lectures/module01').exists()
    assert Path('homeworks/hw01_image_filters').exists()

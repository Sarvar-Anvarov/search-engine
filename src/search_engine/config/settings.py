from pathlib import Path
from search_engine import models

THIS_DIR = Path(__file__).resolve(strict=True).parent
ROOT_DIR = THIS_DIR.parent.parent.parent

# Number of response products from search engine
SE_N = 5

# Model options
MODELS_MAPPING = {
    x().name: x for x in models.__all__
}

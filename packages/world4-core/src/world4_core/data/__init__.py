"""Data ingestion: turn a pymrio IOSystem into a :class:`world4_core.mrio.MrioModel`."""

from world4_core.data.download import download_exiobase
from world4_core.data.loaders import load_exiobase_model, load_test_model

__all__ = ["download_exiobase", "load_exiobase_model", "load_test_model"]

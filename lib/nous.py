# --- IMPORTS ---

import os
import pandas as pd
from xdg import (
    XDG_CONFIG_HOME,
    XDG_CACHE_HOME,
    XDG_DATA_HOME,
)
from contextlib import contextmanager
from typing import Union


# --- VARIABLES ---

CONFIG_PATH = os.path.join(XDG_CONFIG_HOME, "nous")
CACHE_PATH = os.path.join(XDG_CACHE_HOME, "nous")
DATA_PATH = os.path.join(XDG_DATA_HOME, "nous")


# --- CONTEXT MANAGER ---

@contextmanager
def open_df(filename):
    df = pd.read_csv(filename)
    # TODO: Fix no file.
    try:
        return df
    finally:
        df.to_csv(filename)


# --- CLASSES ---

class Ressources():
    def __init__(self):
        self.path = os.path.join(DATA_PATH, "ressources.csv")

    def put(self, url: str) -> None:
        """Put a URL to the ressources.
        """
        # TODO: Fix POST to PUT.
        with open_df(self.path) as df:
            df.append({"url": url}, ignore_index=True)

    def get(self, index: int = None) -> Union[str, list]:
        """Get a URL from the ressources.


        """
        with open_df(self.path) as df:
            match = df.index if index is None else df.index == index
            return df[match].to_dict("records")

ressources = Ressources()

class Tags():
    pass
tags = Tags()

class Semantic():
    pass
semantic = Semantic()


# --- MAIN ---

if __name__ == "__main__":
    pass
    print(str(CONFIG_PATH))
    print(str(CACHE_PATH))
    print(str(DATA_PATH))
    ressources.put("https://cybertutor.de")
    print(ressources.get())


# import Packages
import argparse          # reads options typed after the file name, like --train
import csv               # reads the optional trailer_map.csv file
import getpass           # asks for a password without showing it on screen
import hashlib           # provides PBKDF2 for hashing passwords
import hmac              # safe comparison of two hashes
import json              # parses the JSON-like text inside the TMDB CSV
import pickle            # saves and loads the trained model to disk
import random            # random sampling for exploration
import re                # checks username format with a pattern
import secrets           # makes random salts for passwords
import sqlite3           # the database engine (built into Python)
import sys               # used to exit with a status code
import uuid              # makes a unique id for each batch of recommendations
import webbrowser        # opens the YouTube trailer in the browser
from collections import Counter
from contextlib import contextmanager
from pathlib import Path
from urllib.parse import urlparse

# Matplotlib draws the Elbow chart. "Agg" means "draw to a file, don't open a window".
# The notebook switches the backend back to inline so charts show up there.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler


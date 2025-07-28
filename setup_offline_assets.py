# setup_offline_assets.py

import nltk
from sentence_transformers import SentenceTransformer
import os

print("--- Starting download of offline assets ---")

# --- 1. SETUP PATHS ---
# These paths MUST match the ENV variables in the Dockerfile
MODEL_CACHE_DIR = "/app/model_cache"
NLTK_DATA_DIR = "/app/nltk_data"

# --- 2. DOWNLOAD AND CACHE THE SENTENCE TRANSFORMER MODEL ---
print(f"Downloading and caching the e5-base-v2 model to: {MODEL_CACHE_DIR}")
# By passing the cache_folder, we tell the library exactly where to save the files.
SentenceTransformer('intfloat/e5-base-v2', cache_folder=MODEL_CACHE_DIR)
print("Model download complete.")

# --- 3. DOWNLOAD AND CACHE NLTK DATA ---
print(f"Downloading and caching NLTK data to: {NLTK_DATA_DIR}")
nltk.download('wordnet', download_dir=NLTK_DATA_DIR)
nltk.download('averaged_perceptron_tagger', download_dir=NLTK_DATA_DIR)
nltk.download('punkt', download_dir=NLTK_DATA_DIR)
print("NLTK data download complete.")

print("--- Offline assets are ready. ---")
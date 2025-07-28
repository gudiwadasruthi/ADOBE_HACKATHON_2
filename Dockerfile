# Use a specific, stable, and lightweight version of Python for reproducibility.
FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

# --- 1. INSTALL SYSTEM DEPENDENCIES ---
RUN apt-get update && apt-get install -y tesseract-ocr && rm -rf /var/lib/apt/lists/*

# --- 2. INSTALL PYTHON LIBRARIES ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- 3. PRE-DOWNLOAD OFFLINE ASSETS (THE FOOLPROOF METHOD) ---
# Define the environment variables so our main script knows where to look at RUNTIME.
ENV SENTENCE_TRANSFORMERS_HOME=/app/model_cache
ENV NLTK_DATA=/app/nltk_data

# Copy and run our single, dedicated setup script.
# This avoids all complex shell quoting issues.
COPY setup_offline_assets.py .
RUN python setup_offline_assets.py

# --- 4. COPY MAIN SOURCE CODE ---
COPY heading_extractor.py .
COPY analyze_collections.py .
COPY process_pdfs.py .

# --- 5. DEFINE THE RUN COMMAND ---
CMD ["python", "process_pdfs.py"]
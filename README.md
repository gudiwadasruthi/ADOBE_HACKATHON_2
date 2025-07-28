# PDF Extractor and Semantic Analysis Solution

## Approach Explanation: A Multi-Stage, Semantics-Driven Analysis Engine

Our solution for the "Connecting the Dots" challenge is designed to function as an intelligent document analyst, moving beyond simple text extraction to deliver true contextual relevance. The core of our approach is a sophisticated, modular pipeline that first understands the user's intent on a deep level and then uses that understanding to find, rank, and present the most useful information from a collection of documents.

### Key Components:

1. **NLP-Powered Query Expansion**
   - Uses NLTK and WordNet for dynamic query expansion
   - Enriches queries with relevant synonyms and semantically related terms
   - Ensures comprehensive, context-aware search

2. **Deep Semantic Analysis**
   - Powered by intfloat/e5-base-v2 sentence-embedding model
   - Converts queries and document content into "meaning vectors"
   - Runs efficiently offline on CPU

3. **Multi-Factor Ranking**
   - "Best Sections" list (50% title + 50% content relevance)
   - "Best Content" list (content-only relevance)
   - Mimics human expert evaluation

## Docker Setup and Execution

### Build the Docker Image
```bash
docker build --platform linux/amd64 -t adobe-hackathon-solution .
```

### Run the Solution
```bash
docker run --rm \
  -v "$(pwd)/input:/app/input:ro" \
  -v "$(pwd)/output:/app/output" \
  --network none \
  adobe-hackathon-solution
```

### Requirements:
- Input directory containing:
  - PDF documents
  - challenge1b_input.json
- Empty output directory for results

### Notes:
- Runs fully offline once built
- Processes all PDFs in input directory
- Generates structured JSON output in output directory

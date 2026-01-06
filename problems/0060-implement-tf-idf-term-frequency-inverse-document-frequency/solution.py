import numpy as np
from collections import Counter
def compute_tf_idf(corpus, query):
	"""
	Compute TF-IDF scores for a query against a corpus of documents.
    
	:param corpus: List of documents, where each document is a list of words
	:param query: List of words in the query
	:return: List of lists containing TF-IDF scores for the query words in each document
	"""
    # Handle empty corpus
    if not corpus:
        return []

    tf_counters = []
    df_counts = {}
    doc_count = len(corpus)

    # Compute term frequencies (counters) and document frequencies (DF)
    for doc in corpus:
        if not doc:
            tf = Counter()
        else:
            tf = Counter(doc)
        tf_counters.append(tf)
        for term in tf.keys():
            df_counts[term] = df_counts.get(term, 0) + 1

    # Compute inverse document frequency (IDF) with smoothing: idf = log((N+1)/(df+1)) + 1
    idf = {}
    for term, df in df_counts.items():
        idf[term] = np.log((doc_count + 1) / (df 
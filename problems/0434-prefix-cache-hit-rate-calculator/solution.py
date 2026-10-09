def prefix_cache_hit_rate(prompts: list, cache: list) -> dict:
    """
    Calculate the prefix cache hit rate for a batch of tokenized prompts.

    Args:
        prompts: List of tokenized prompts (list of list of ints).
        cache: List of cached prefixes (list of list of ints).

    Returns:
        Dictionary with 'hit_rate', 'cached_tokens', and 'total_tokens'.
    """
    # count how many tokens before caching
    total_tokens = sum(len(prompt) for prompt in prompts)

    # initiate count for chached tokens
    cached_tokens = 0

    # iterate each prompt, and find how many tokens can be cached using given cache
    for prompt in prompts:
        best_matched = 0 # initiate match
        for ch in cache: # check each token in cache
            if len(ch) <= len(prompt) and prompt[:len(ch)] == ch:
                best_matched = max(best_matched, len(ch)) # update number of matched cache tokens
        cached_tokens += best_matched # accumulated matched token
    
    hit_rate = round(cached_tokens / total_tokens, 4) if total_tokens > 0 else 0.0

    return {'hit_rate': hit_rate, 'cached_tokens': cached_tokens, 'total_tokens': total_tokens}


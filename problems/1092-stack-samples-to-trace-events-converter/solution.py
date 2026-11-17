def stacks_to_trace(samples):
    # samples: list of [timestamp, [frame_outer, ..., frame_inner]]
    # return: list of (timestamp, action, frame_name) tuples
    # Idea: a frame is "still active" only if it sits at the same depth AND every frame above it (towards the root) is also unchanged 
    # -> the longest common  PREFIX of the previous and current stacks. 
    # Everything after that prefix in prev has ended; everything after it in cur has started.

    events = []
    # if no event is executing, return empty list
    if not samples:
        return events
    
    # construct a prev stack to trace levels up
    prev = []

    for ts, stack in samples:
        # 1. length of the longest common prefix
        k = 0
        # check how long the prefix can safely go
        limit = min(len(prev), len(stack))
        while k < limit and prev[k] == stack[k]:
            k += 1
        # 2. frames that ended: prev[k:], innermost first
        for i in range(len(prev)-1, k-1, -1):
            events.append((ts, "end", prev[i]))
        # 3. frames that started: stack[k:], outermost first
        for i in range(k, len(stack)):
            events.append((ts, "start", stack[i]))
        # the current sample will be compared against next
        prev = stack
    
    # 4. close whatever is still open at the last timestamp, innermost first
    last_ts = samples[-1][0]
    for i in range(len(prev)-1, -1, -1):
        events.append((ts, "end", prev[i]))
    
    return events


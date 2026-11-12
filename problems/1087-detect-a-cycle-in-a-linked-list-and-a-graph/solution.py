def detect_cycles(ll_next, graph):
    # ll_next: list of next-node indices, -1 means null, start at node 0
    # graph: adjacency list of a directed graph
    # return (entry_index_or_-1, graph_has_cycle_bool)

    # 1: single linked list -- use fast/slow pointer
    # edge case: no nodes --> no cycle, returns -1 for entry
    entry = -1
    if ll_next:
        slow = fast = 0
        # before fast pointer reaches the end
        while fast != -1 and ll_next[fast] != -1:
            # slow moves one node, fast moves two nodes
            slow = ll_next[slow]
            fast = ll_next[ll_next[fast]]
            # if slow & fast meet -> cycle detected, find entry
            if slow == fast:
                # reset slow pointer to first index
                slow = 0
                # re-initiate the traversal, both pointers one at a time
                while slow != fast:
                    slow = ll_next[slow]
                    fast = ll_next[fast]
                # cycle --> slow and fast will meet at slow pointer as cycle entry
                entry = slow
                break
    
    # 2: directed graph -- use DFS traversal: stop as soon as finding cycles
    # initiate three flags:
    # UNVISITED flags the univisted nodes
    # ENCOUNTERED flags the node encountered but not finished
    # FINISHED flags the node whose all edges have been explored
    UNVISITED, ENCOUNTERED, FINISHED = 0, 1, 2
    n = len(graph)
    flags = [UNVISITED] * n

    has_cycle = False

    for start in range(n):
        # skip nodes that have been explored
        if flags[start] != UNVISITED:
            continue
        # mark start of a DFS encountered until ALL edges have been explored
        flags[start] = ENCOUNTERED
        # create the DFS where start is the only entry, create iter tool for all neighboring edges where thid node is the entry
        stack = [(start, iter(graph[start]))]
        # traverse DFS using stack
        while stack and not has_cycle:
            node, neighbors = stack[-1]
            nxt = next(neighbors, None)
            # if next is None, all edges have been explored, flag node as finished
            if nxt is None:
                flags[node] = FINISHED
                stack.pop()
            # if next has been marked as encounterd, there is a cycle
            elif flags[nxt] == ENCOUNTERED:
                has_cycle = True
            # if next is unvisited, push its neighboring edges in the stack
            elif flags[nxt] == UNVISITED:
                stack.append((nxt, iter(graph[nxt])))
        
        if has_cycle:
                break
    
    return (entry, has_cycle)






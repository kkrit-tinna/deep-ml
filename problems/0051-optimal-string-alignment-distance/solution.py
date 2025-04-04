def OSA(s1, s2):
    m, n = len(s1), len(s2)
    
    # Create a 2D array to store the OSA distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the base cases
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters from s1
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters into s1 to form s2
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No edit needed
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,   # Deletion
                    dp[i][j - 1] + 1,   # Insertion
                    dp[i - 1][j - 1] + 1 # Substitution
                )
            
            # Check for transposition
            if i > 1 and j > 1 and s1[i - 2:i] == s2[j - 2:j][::-1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1) # Transposition
    
    return d
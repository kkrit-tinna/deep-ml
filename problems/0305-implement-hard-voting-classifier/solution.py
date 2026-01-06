import numpy as np
def hard_voting_classifier(predictions: list[list[int]]) -> list[int]:
    """
    Implement a hard voting classifier using majority vote.
    
    Args:
        predictions: 2D list where predictions[i][j] is classifier i's prediction for sample j
        
    Returns:
        List of final predictions using majority vote
    """
    votes = np.array(predictions).T

    final_predictions = []
    for vote in votes:
        final_predictions.append(np.argmax(np.bincount(vote)))
    
    return final_predictions
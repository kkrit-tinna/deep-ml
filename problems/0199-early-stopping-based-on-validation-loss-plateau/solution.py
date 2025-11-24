def early_stopping(val_losses: list[float], patience: int = 5, min_delta: float = 0.0) -> list[bool]:
	"""
	Determine at each epoch whether training should stop based on validation loss.
	
	Args:
		val_losses: List of validation losses at each epoch
		patience: Number of epochs to wait for improvement before stopping
		min_delta: Minimum change in validation loss to qualify as improvement
	
	Returns:
		List of booleans indicating whether to stop at each epoch
	"""
    res = []
    best_loss = float('inf') # minimize
    last_improvement = -1

    for epoch, loss in enumerate(val_losses):
        if loss < best_loss - min_delta:
            best_loss = loss
            last_improvement = epoch

        res.append(epoch - last_improvement >= patience)

    return res
from typing import Tuple

def early_stopping(val_losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:
    best_epoch = -1 # start with -1 as 'pre-head'
    best_loss = float('inf')
    no_improv_epoch = 0

    for epoch, loss in enumerate(val_losses):
        # update ONLY when loss has improved upon threshold
        if loss < best_loss - min_delta:
            best_loss = loss
            best_epoch = epoch
            no_improv_epoch = 0 # need to reset counting of no improvemnt
        else: # keep track of epochs without improvement
            no_improv_epoch += 1
    
        if no_improv_epoch >= patience:
            return epoch, best_epoch
    
    return len(val_losses)-1, best_epoch # return the length of losses if no improvement ever
        



    
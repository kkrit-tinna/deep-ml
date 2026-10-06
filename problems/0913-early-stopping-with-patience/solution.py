class EarlyStopping:
    def __init__(self, patience: int, mode: str = 'min'):
        self.patience = patience
        self.mode = mode
        self.best = float('inf') if mode == 'min' else float('-inf')
        self.bad_step = 0

    def step(self, metric: float) -> bool:
        if self.mode == 'min':
            improved = metric < self.best
        else:
            improved = metric > self.best
        
        if improved:
            self.best = metric # update
            self.bad_step = 0 # reset
            return False
        else:
            self.bad_step += 1
            return self.bad_step >= self.patience


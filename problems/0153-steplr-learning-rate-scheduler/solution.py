class StepLRScheduler:
    def __init__(self, initial_lr, step_size, gamma):
        self.initial_lr = initial_lr
        self.step_size = step_size
        self.gamma = gamma

    def get_lr(self, epoch):
        lr = self.initial_lr * (self.gamma**(epoch // self.step_size))

        return round(lr, 4)
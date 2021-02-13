from tensorflow.keras.callbacks import Callback

class ReachAccuracyStop(Callback):

  def __init__(self, accuracy):
    super().__init__()
    self.accuracy = accuracy

  def on_epoch_end(self, epoch, logs=None):
    if logs.get('acc') > self.accuracy:
      print(f"\nReached {self.accuracy}% accuracy so stopping training!")
      self.model.stop_training = True
    return super().on_epoch_end(epoch, logs=logs)
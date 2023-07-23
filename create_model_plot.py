import matplotlib.pyplot as plt
from matplotlib import style


style.use("ggplot")


def create_acc_loss_graph(model_name):
  content = open("model.log").read().split("\n")

  times, accs, losses, val_acss, val_losses = [], [], [], [], []

  for c in content:
    if model_name not in c:
      continue

    _, time, acc, loss, val_acc, val_loss = c.split(",")

    times.append(float(time))
    accs.append(float(acc))
    losses.append(float(loss))
    val_acss.append(float(val_acc))
    val_losses.append(float(val_loss))

  
  fig = plt.figure()

  ax1 = plt.subplot2grid((2, 1), (0, 0))
  ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)


  ax1.plot(times, accs, label="acc")
  ax1.plot(times, val_acss, label="val_acc")
  ax1.legend(loc=2)
  ax2.plot(times, losses, label="loss")
  ax2.plot(times, val_losses, label="val_loss")
  ax2.legend(loc=2)
  plt.show()

model_name = "model-1690102556"
create_acc_loss_graph(model_name)
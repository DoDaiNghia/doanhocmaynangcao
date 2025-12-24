import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("log_vietocr.csv")

plt.plot(df["iteration"], df["train_loss"], label="Train Loss")
plt.plot(df["iteration"], df["valid_loss"], label="Valid Loss")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.legend()
plt.title("Loss over Iterations")
plt.grid(True)
plt.show()

plt.plot(df["iteration"], df["acc_full_seq"], label="Full Seq Accuracy")
plt.plot(df["iteration"], df["acc_per_char"], label="Per Char Accuracy")
plt.xlabel("Iteration")
plt.ylabel("Accuracy")
plt.legend()
plt.title("Accuracy over Iterations")
plt.grid(True)
plt.show()

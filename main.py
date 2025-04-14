import pandas as pd
import seaborn as sns

if __name__ == "__main__":
    df = sns.load_dataset("titanic")
    df.to_csv("snstitanic.csv")

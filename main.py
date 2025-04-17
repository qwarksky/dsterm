import pandas as pd
import polars as pl
import seaborn as sns

pl.Config.set_tbl_cols(-1)


def pdinfo(df_: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Index": [df_.columns.get_loc(col) for col in df_.columns],
            "DTYPES": df_.dtypes,
            "COUNT": df_.count(),
            "NUNIQUE": df_.nunique(),
            "NULLNA": df_.isnull().sum(),
            "LEN_MAX": [df_[col].astype(str).str.len().max() for col in df_.columns],
            "LEN_MIN": [df_[col].astype(str).str.len().min() for col in df_.columns],
            "WORDS_MAX": [
                df_[col].astype(str).apply(lambda x: len(x.split())).unique().max()
                for col in df_.columns
            ],
            "WORDS_MIN": [
                df_[col].astype(str).apply(lambda x: len(x.split())).unique().min()
                for col in df_.columns
            ],
        }
    ).sort_values(by="NUNIQUE", ascending=True)


def plinfo(df_: pl.DataFrame) -> pl.DataFrame:
    print(f"""DataFrame Shape:{df_.shape}""")
    return pl.DataFrame(
        {
            "DTYPES": df_.dtypes,
            "FEATURES": df_.columns,
            "COUNT": df_.select(pl.all().count()).transpose(),
            "NUNIQUES": df_.select(pl.all().n_unique()).transpose(),
            "NULLS": df_.select(pl.all().null_count()).transpose(),
            "TOP": df_.max().transpose(),
            "BOTTOM": df_.min().transpose(),
            "WORDS": df_.select(
                pl.all().cast(pl.String).str.split(" ").list.len().sum()
            ).transpose(),
            "WORDS_min": df_.select(
                pl.all().cast(pl.String).str.split(" ").list.len().min()
            ).transpose(),
            "WORDS_mean": df_.select(
                pl.all().cast(pl.String).str.split(" ").list.len().mean()
            ).transpose(),
            "WORDS_max": df_.select(
                pl.all().cast(pl.String).str.split(" ").list.len().max()
            ).transpose(),
            "WORDS_median": df_.select(
                pl.all().cast(pl.String).str.split(" ").list.len().median()
            ).transpose(),
            "LEN_max": df_.select(
                pl.all().cast(pl.String).str.len_chars().max()
            ).transpose(),
            "LEN_min": df_.select(
                pl.all().cast(pl.String).str.len_chars().min()
            ).transpose(),
            "LEN_mean": df_.select(
                pl.all().cast(pl.String).str.len_chars().mean()
            ).transpose(),
            "LEN_median": df_.select(
                pl.all().cast(pl.String).str.len_chars().median()
            ).transpose(),
        }
    ).sort(by="COUNT", descending=True)


if __name__ == "__main__":
    df = sns.load_dataset("titanic")
    # df.to_csv("snstitanic.csv")

    print("PANDAS PDINFO")
    print(df.pipe(pdinfo))

    print("-----------------------------------------\n")

    print("POLARS PLINFO")
    print(pl.from_pandas(df).pipe(plinfo))

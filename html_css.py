import pandas as pd
from IPython.core.display import display_html


def unite_dataframes_col(df1, df2, col1_title, col2_title, replace_NAN=None):
    df3 = pd.concat([df1, df2], axis=1, keys=[str(col1_title), str(col2_title)])
    if replace_NAN is not None:
        df3 = df3.fillna(replace_NAN)
    return df3

css1 = {
    "selector": "td:hover",
    "props": "text-align: center; font-size: 120%; font-weight: bold; color: black; background-color: #ffffb3;"
}
css2 = {
    'selector': '.index_name',
    'props': 'font-style: italic; color: black; font-weight:normal;'
}
css3 = {
    'selector': 'th:not(.index_name)',
    'props': 'background-color: #000066; color: white;'
}
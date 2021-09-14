import pandas as pd
from IPython.core.display import display_html


def df_style(datafram1, datafram2, titulo1='titulo1', titulo2='titulo2'):
    try:
        datafram1S=datafram1.style.set_table_attributes\
            ("style='display:inline'").set_table_styles(table_styles = [dict(selector="caption",
            props=[("text-align", "center"),
            ("font-size", "120%"),
            ("color", 'black')])]).set_caption(titulo1)

        datafram2S=datafram2.style.set_table_attributes\
            ("style='display:inline'").set_table_styles(table_styles = [dict(selector="caption",
            props=[("text-align", "center"),
            ("font-size", "120%"),
            ("color", 'black')])]).set_caption(titulo2)
    except Exception:
        pass
    display_html(datafram1S._repr_html_() + "\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0" + datafram2S._repr_html_(), raw=True)


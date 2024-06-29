# %%
from function import *

# %%
df = load_data_with_column_order('df_migros.csv', ['city', 'population', 'coordinates', 'migros_count'])

# %%
df = format_df(df)

# %%
create_plot(df)

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

def load_data_with_column_order(file_path, col_order):
    df_migros = pd.read_csv(file_path)
    df = df_migros[col_order].copy()
    return df

def format_df(df):
    df['pop_to_stores'] = df['population'] / df['migros_count']
    df['lat'] = df['coordinates'].apply(lambda x: float(x.replace(",","").split(" ")[0]))
    df['lon'] = df['coordinates'].apply(lambda x: float(x.replace(",","").split(" ")[1]))
    df = df[df['population']>0].sort_values(by='pop_to_stores').reset_index(drop=True)
    return df


def create_plot(df):
    average_ratio = int(df['pop_to_stores'].mean())
    average_ratio_formatted = "{:,.0f}".format(average_ratio)
    fig = px.scatter_mapbox(df, 
                            lat="lat", 
                            lon="lon", 
                            hover_name="city", 
                            hover_data = {'pop_to_stores': True, 'lat': False, 'lon': False, 'migros_count': True},
                            zoom=6.5, 
                            opacity=0.8,
                            mapbox_style='carto-positron',
                            size="pop_to_stores",
                            color="pop_to_stores",
                            color_continuous_scale="RdYlGn",
                            height=500,
                            width=950,
                        )
    fig.update_layout(mapbox=dict(center=dict(lat=46.8, lon=8.15)))
    fig.update_layout(margin=dict(l=0, r=10, t=100, b=10))
    fig.update_layout(
        title=f'<b>Population-to-supermarkets ratio</b><br>'
            f'<span style="font-size:14px">By city (Switzerland) - average: {average_ratio_formatted}</span><br>',
        coloraxis_colorbar=None
    )
    pio.write_html(fig, file='plot.html', auto_open=False)

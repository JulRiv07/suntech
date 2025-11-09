import pandas as pd
import plotly.graph_objects as go


try:
    df = pd.read_csv('12 solar-energy-consumption.csv')
except FileNotFoundError:
    print("Error: No se encontró el archivo '12 solar-energy-consumption.csv'")
    exit()

df_sorted = df.sort_values(by='Electricity from solar (TWh)', ascending=False)

fig = go.Figure(go.Bar(
    x=df_sorted['Entity'],                   
    y=df_sorted['Electricity from solar (TWh)'],  
    textposition='auto'
))


fig.update_layout(
    title='Producción de Electricidad Solar por Región (2021)',
    xaxis_title='Región / País',
    yaxis_title='Electricidad (TWh)'
)

fig.write_html('grafica_barras_solar.html')

print("¡Gráfica interactiva 'grafica_barras_solar.html' guardada con éxito!")
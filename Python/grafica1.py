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
    textposition='auto',
    marker_color="orange"
))


fig.update_layout(

    xaxis_title='Región / País',
    yaxis_title='Electricidad (TWh)'
)

fig.write_html('grafica_barras_solar.html')

print("¡Gráfica interactiva 'grafica_barras_solar.html' guardada con éxito!")
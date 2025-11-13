import pandas as pd
import plotly.graph_objects as go

try:
    df = pd.read_csv('13 installed-solar-PV-capacity.csv')
except FileNotFoundError:
    print("Error: No se encontró el archivo '13 installed-solar-PV-capacity.csv'")
    exit()

df['Solar Capacity'] = df['Solar Capacity'].astype(str).str.replace('.', '', regex=False)
df['Solar Capacity'] = pd.to_numeric(df['Solar Capacity'])
df_sorted = df.sort_values(by='Solar Capacity', ascending=False)



fig = go.Figure(go.Pie(
    labels=df_sorted['Entity'],       
    values=df_sorted['Solar Capacity'], 
    textinfo='percent+label'            
))


fig.update_layout(
    template='plotly_white'
)


fig.write_html('grafica_pastel_solar.html') 
print("¡Gráfica interactiva 'grafica_pastel_solar.html' guardada con éxito!")
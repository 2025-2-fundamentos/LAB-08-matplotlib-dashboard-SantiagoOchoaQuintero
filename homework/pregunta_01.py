# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    # --- Configuración de Rutas ---
    # Instrucción específica: El archivo está en la carpeta 'data'
    DATA_FILE = 'files/input/shipping-data.csv'
    OUTPUT_DIR = 'docs'
    DASHBOARD_FILE = os.path.join(OUTPUT_DIR, 'index.html')

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Cargar datos
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        # Fallback por si se ejecuta en un entorno con estructura diferente
        return

    # --- 1. Shipping per Warehouse (Gráfico de Barras) ---
    plt.figure()
    counts = df.Warehouse_block.value_counts()
    counts.plot(kind='bar')
    plt.title('Shipping per Warehouse')
    plt.xlabel('Warehouse block')
    plt.ylabel('Record count')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'shipping_per_warehouse.png'))
    plt.close()

    # --- 2. Mode of Shipment (Gráfico de Dona) ---
    plt.figure()
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot(
        kind='pie',
        figsize=(6, 6),
        wedgeprops=dict(width=0.35),
        ylabel='',
        colors=['tab:blue', 'tab:orange', 'tab:green']
    )
    plt.title('Mode of Shipment')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'mode_of_shipment.png'))
    plt.close()

    # --- 3. Average Customer Rating (Gráfico de Barras Horizontales) ---
    plt.figure()
    # El video agrupa por Mode_of_Shipment y calcula el promedio (mean)
    stats = df.groupby('Mode_of_Shipment')['Customer_rating'].mean()
    stats.plot(kind='barh', color='tab:orange')
    plt.title('Average Customer Rating')
    plt.xlabel('Rating')
    plt.ylabel('Mode of Shipment')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_color('gray')
    plt.gca().spines['bottom'].set_color('gray')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'average_customer_rating.png'))
    plt.close()

    # --- 4. Weight Distribution (Histograma) ---
    plt.figure()
    df.Weight_in_gms.plot(kind='hist', bins=20, color='tab:orange', edgecolor='white')
    plt.title('Shipped Weight Distribution')
    plt.xlabel('Weight in gms')
    plt.ylabel('Frequency')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'weight_distribution.png'))
    plt.close()

    # --- 5. Generar HTML ---
    html_content = """<!DOCTYPE html>
<html>
    <body>
        <h1>Shipping Dashboard Example</h1>
        <div style="width:45%;float:left">
            <img src="shipping_per_warehouse.png" alt="Fig 1">
            <img src="mode_of_shipment.png" alt="Fig 2">
        </div>
        <div style="width:45%;float:left">
            <img src="average_customer_rating.png" alt="Fig 3">
            <img src="weight_distribution.png" alt="Fig 4">
        </div>
    </body>
</html>
"""
    with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
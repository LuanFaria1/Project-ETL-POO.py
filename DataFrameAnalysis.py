import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalyzer:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def analyze(self):
        print("1. Quantidade de elementos:", len(self.data_frame))
        print("\n2. Nome das colunas:", self.data_frame.columns.tolist())
        print("\n3. Tipo de dado das colunas:")
        print(self.data_frame.dtypes)
        print("\n4. Análise estatística dos dados:")
        print(self.data_frame.describe().apply(lambda x: round(x, 2)))
        print("\n5. Mediana:")
        print(self.data_frame.median())
        print("\n6. Coeficiente de Variação:")
        for column in self.data_frame.select_dtypes(include=['number']).columns:
            coef_variacao = (self.data_frame[column].std() / self.data_frame[column].mean()) * 100
            print(f"{column}: {coef_variacao:.2f}%")
        print("\n7. Desvio Padrão:")
        for column in self.data_frame.select_dtypes(include=['number']).columns:
            print(f"{column}: {self.data_frame[column].std():.2f}")

class DataVisualizer:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def plot_distribution(self, columns):
        for column in columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(self.data_frame[column], kde=True, color='g')
            plt.title(f'Distribuição Normal de {column}')
            plt.xlabel(column)
            plt.ylabel('Densidade')
            plt.grid(True)
            plt.show()

    def plot_boxplot(self, columns):
        for column in columns:
            plt.figure(figsize=(6, 4))
            sns.boxplot(x=self.data_frame[column])
            plt.title(f'Boxplot de {column}')
            plt.xlabel(column)
            plt.grid(True)
            plt.show()

    def plot_index_vs_time(self, column_tempo, columns_indice):
        for column_indice in columns_indice:
            plt.figure(figsize=(10, 5))
            plt.plot(self.data_frame[column_tempo], self.data_frame[column_indice], color='b')
            plt.title(f'Curva {column_indice} vs Tempo')
            plt.xlabel('Tempo')
            plt.ylabel(column_indice)
            plt.grid(True)
            plt.show()

try:
    df = pd.read_excel("DataFramePOO.xlsx")
except FileNotFoundError:
    print("Arquivo não encontrado.")
    df = pd.DataFrame()

if not df.empty:
    analyzer = DataAnalyzer(df)
    analyzer.analyze()

    visualizer = DataVisualizer(df)
    visualizer.plot_distribution(['Total'])
    visualizer.plot_boxplot(['Total'])
    visualizer.plot_index_vs_time('Data', ['Total'])

print(df)

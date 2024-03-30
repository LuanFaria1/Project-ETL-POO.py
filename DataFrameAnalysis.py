import pandas as pd
import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self, data_frame):
        self.data_frame = data_frame
    
    def analyze(self): 
        print("1. Quantidade de elementos:")
        print(len(self.data_frame))
        print("\n2. Nome das colunas:")
        print(self.data_frame.columns.tolist())
        print("\n3. Tipo de dado das colunas:")
        print(self.data_frame.dtypes)
        print("\n4. Análise estatística dos dados:")
        print(self.data_frame.describe().apply(lambda x: round(x, 2)))

class DataVisualizer:
    def __init__(self, data_frame):
        self.data_frame = data_frame
    
    def plot_distribution(self, column):
        plt.figure(figsize=(8, 6))
        plt.hist(self.data_frame[column], bins=30, density=True, alpha=0.6, color='g')
        plt.title(f'Distribuição Normal de {column}')
        plt.xlabel(column)
        plt.ylabel('Densidade')
        plt.grid(True)
        plt.show()

    def plot_boxplot(self, column):
        plt.figure(figsize=(6, 4))
        plt.boxplot(self.data_frame[column])
        plt.title(f'Boxplot de {column}')
        plt.ylabel(column)
        plt.grid(True)
        plt.show()

    def plot_index_vs_time(self, column):
        tempo = range(len(self.data_frame))
        indices = self.data_frame[column]
        plt.figure(figsize=(10, 5))
        plt.plot(tempo, indices, color='b')
        plt.title(f'Curva {column} vs Tempo')
        plt.xlabel('Tempo')
        plt.ylabel(column)
        plt.grid(True)
        plt.show()

# Carregar os dados
df = pd.read_excel("DataFramePOO.xlsx")

# Analisar os dados
analyzer = DataAnalyzer(df)
analyzer.analyze()

# Visualizar os dados
visualizer = DataVisualizer(df)
visualizer.plot_distribution('Total')
visualizer.plot_boxplot('Total')
visualizer.plot_index_vs_time('Total')

print(df)

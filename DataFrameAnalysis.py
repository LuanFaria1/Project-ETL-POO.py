# Define as classes para extração, análise e cálculo estatístico
import pandas as pd

class DataExtractor:
    def __init__(self, file_path):
        self.data = pd.read_excel(file_path)
    
    def extract(self):
        return self.data

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
        print(self.data_frame.describe())

class MediaCalculator:
    def __init__(self, data_frame):
        self.data_frame = data_frame
    
    def calcular_media(self, coluna):
        media = round(self.data_frame[coluna].mean(), 2)
        print(f"\nMédia da coluna '{coluna}': {media}")

class MedianaCalculator:
    def __init__(self, data_frame):
        self.data_frame = data_frame
    
    def calcular_mediana(self, coluna):
        mediana = round(self.data_frame[coluna].median(), 2)
        print(f"\nMediana da coluna '{coluna}': {mediana}")

class DesvioPadraoCalculator:
    def __init__(self, data_frame):
        self.data_frame = data_frame
    
    def calcular_desvio_padrao(self, coluna):
        desvio_padrao = round(self.data_frame[coluna].std(), 2)
        print(f"\nDesvio padrão da coluna '{coluna}': {desvio_padrao}")

# Realiza as operações
if __name__ == "__main__":
    file_path = "DataFramePOO.xlsx" 

    # Extração de dados
    extractor = DataExtractor(file_path)
    extracted_data = extractor.extract()

    # Análise estatística
    analyzer = DataAnalyzer(extracted_data)
    analyzer.analyze()

    # Cálculo da média
    calculator_media = MediaCalculator(extracted_data)
    calculator_media.calcular_media('Total')  

    # Cálculo da mediana
    calculator_mediana = MedianaCalculator(extracted_data)
    calculator_mediana.calcular_mediana('Total')  

    # Cálculo do desvio padrão
    calculator_desvio_padrao = DesvioPadraoCalculator(extracted_data)
    calculator_desvio_padrao.calcular_desvio_padrao('Total') 

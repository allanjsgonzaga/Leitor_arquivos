#Importando bibliotecas para que seja verificar se o arquivo existe e consequentemente para manipular arquivos e diretórios
from pathlib import Path
from pydoc import doc
import statistics

#Importando biblioteca para expressões regulares(Para que os numeros sejam extraídos do texto)
import re 

#Importando biblioteca para manipular arquivos do Word
from docx import Document # type: ignore

#biblioteca para manipular arquivos PDF
import PyPDF2 # type: ignore


#Caminhos dos arquivos
folder_docx = Path("D:/Users/ALLAN/documents/arquivo.docx") #Caminho do arquivo .docx
folder_pdf = Path("D:/Users/ALLAN/documents/arquivo.pdf") #Caminho do arquivo .pdf

#Função para extrair texte de arquivos .docx
def extract_text_from_docx(folder):
    doc = Document(folder) #Lendo o arquivo .docx
    return "\n".join([par.text for par in doc.paragraphs]) #Retorna o texto do arquivo .docx

#Função para extrair texto de arquivos .pdf
def extract_text_from_pdf(folder2):
    text = ""
    with open(folder2, "rb") as file: #Abrindo o arquivo .pdf
        reader = PyPDF2.PdfReader(file) #Lendo o arquivo .pdf
        for page in reader.pages: #Iterando sobre as páginas do arquivo .pdf
            text += page.extract_text() + "\n"
    return text #Retorna o texto do arquivo .pdf

#Verificando se o arquivo existe
if folder_docx.exists():
    print("O arquivo .docx existe") #Retorno sobre a existência do arquivo docx
    texto = extract_text_from_docx(folder_docx) #Extraindo o texto do arquivo .docx
elif folder_pdf.exists():
    print("O arquivo .pdf existe") #Retorno sobre a existência do arquivo pdf
    texto = extract_text_from_pdf(folder_pdf) #Extraindo o texto do arquivo .pdf
else:
    print("Nenhum dos arquivos existe") #Retorno sobre a inexistência dos arquivos
    exit()
    
#Extraindo todods os números do texto
finded_numbers = re.findall(r'\b\d+\b', texto)
numbers = [int(n) for n in finded_numbers] #Lista para armazenar os números
    
                
if numbers: #Verificando se a lista não está vazia
    soma = sum(numbers) #Somando os números
    media = soma / len(numbers) #Calculando a média
    mediana = statistics.median(numbers) #Calculando a mediana
    maior = max(numbers) #Encontrando o maior número    
    menor = min(numbers) #Encontrando o menor número
            
    #Exibindo os resultados
    print(f"Soma: {soma}") #Soma dos números
    print(f"Média: {media}") #Média dos números
    print(f"Mediana: {mediana}") #Mediana dos números
    print(f"Maior: {maior}") #Maior número
    print(f"Menor: {menor}") #Menor número
else:
    #Caso a lista esteja vazia, exibe uma mensagem
    print("O arquivo está vazio ou Não há números válidos")

    

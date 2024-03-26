import glob
import subprocess

# Lista todos os arquivos CSV no diretório atual
csv_files = glob.glob('*.csv')

# Para cada arquivo CSV, executa o script genplot.py
for csv_file in csv_files:
    subprocess.run(['python3', 'genplot.py', csv_file])

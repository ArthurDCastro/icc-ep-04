import os
import csv

# Abrir o arquivo L3.log em modo de leitura
def openLog(f):
    with open(f, "r") as file:
        # Ler o conteúdo do arquivo
        return file.read()
    return []


# Iterar pelas regiões
def lerResultados(indicador, out):
    # Dividir a saída em regiões
    regions = out.split("\nRegion ")
    resultados = {}
    for region in regions:
        # Verificar se a região contém informações do indicador
        if indicador in region:
            lines = region.split("\n")
            region_name = lines[0].strip().split(",")[0]
            for line in lines:
                if indicador in line:
                    # Extrair o valor do indicador
                    parts = line.split("|")
                    if parts[1].strip() == indicador:
                        r = float(parts[2].strip())
                        resultados[region_name] = r
    return resultados

def escreverResultados(resultados, diretorio_saida):
    # Iterar pelos indicadores
    for grupo, asd in resultados.items():
        for indicador, valores in asd.items():
            # Criar o nome do arquivo de saída com base no indicador

            os.makedirs(diretorio_saida, exist_ok=True)

            if len(asd) > 1:
                nome_arquivo = f"{diretorio_saida}/{indicador.replace(' ', '-').replace('/', '')}_resultados.csv"
            else:
                nome_arquivo = f"{diretorio_saida}/{grupo}_resultados.csv"
            
            # Abrir o arquivo de saída em modo de escrita
            with open(nome_arquivo, "w", newline="") as csvfile:
                # Cria um escritor CSV
                csv_writer = csv.writer(csvfile)
                
                # Escreve o cabeçalho do CSV com os nomes das regiões
                cabecalho = ["n"]
                if len(valores) > 0:
                    i = list(valores.keys())[0]
                    for regiao in valores[i].keys():
                        cabecalho.append(regiao)
                csv_writer.writerow(cabecalho)


                # Escreve os dados no CSV
                for n, r in valores.items():
                    linha = [n]
                    for valor in r.values():
                        linha.append(valor)
                    csv_writer.writerow(linha)

            print(f"Valores do indicador {indicador} foram escritos no arquivo {nome_arquivo}")


n = [64, 100, 128,  200, 256, 512, 600, 900, 1024, 2000, 2048, 3000, 4000]

ind = {
    "L3": ["L3 bandwidth [MBytes/s]"],
    "L2CACHE": ["L2 miss ratio"],
    "ENERGY": ["Energy [J]"],
    "FLOPS_DP": ["DP MFLOP/s", "AVX DP MFLOP/s"]
}

dir = "resultados/"

resultados = {}

for o, i in ind.items():
    resultados[o] = {}
    for j in i:
        resultados[o][j] = {}

for o, i in ind.items():
    k = 0
    for m in n:
        f = dir + o + "-" + str(m) + ".log"
        if not os.path.isfile(f):
            print(f"O arquivo {f} não foi encontrado.")
        else:
            output = openLog(f)
            for j in i:
                resultados[o][j][str(m)] = lerResultados(j, output)


escreverResultados(resultados, "resultados_finais")
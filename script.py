import os

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

n = {64, 100, 128,  200, 256, 512, 600, 900, 1024, 2000, 2048, 3000, 4000}

ind = {
    "L3": ["L3 bandwidth [MBytes/s]"],
    "L2CACHE": ["L2 miss ratio"],
    "ENERGY": ["Energy [J]"],
    "FLOPS_DP": ["DP MFLOP/s", "AVX DP MFLOP/s"]
}

dir = "resultados/"

resultados = {}

for o, i in ind.items():
    for m in n:
        f = dir + o + ".log"
        if not os.path.isfile(f):
            print(f"O arquivo {f} não foi encontrado.")
        else:
            output = openLog(f)
            resultados[o] = {}
            for j in i:
                resultados[o][j] = lerResultados(j, output)

for i, r in resultados.items():
    print(i)
    j = 0
    for res in r:
        for region, valor in res.items():
            print(f"Região: {region}")
            print(f"{ind[i][j]}: {valor}")
            print()
        j = j + 1

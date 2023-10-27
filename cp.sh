#!/bin/bash

# Caminho para o arquivo de origem
arquivo_origem="resultados/L3.log"

# Diretório de destino para os arquivos copiados
diretorio_destino="resultados"

# Lista de valores de n
valores=("64" "100" "128" "200" "256" "512" "600" "900" "1024" "2000" "2048" "3000" "4000")

# Loop para criar cópias do arquivo de origem
for n in "${valores[@]}"
do
    # Construir o nome do arquivo de destino com base no valor de n
    arquivo_destino="L3-${n}.log"
    
    # Copiar o arquivo de origem para o arquivo de destino com o nome modificado
    cp "${arquivo_origem}" "${diretorio_destino}/${arquivo_destino}"
    echo "Arquivo ${arquivo_origem} copiado para ${diretorio_destino}/${arquivo_destino}"
done

import cv2
import numpy as np
import matplotlib.pyplot as plt

def transformar_para_desenho(imagem, brilho=1.0):
    # Convertendo a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Ajustar o brilho da imagem
    imagem_brilho = cv2.add(imagem_cinza, brilho)

    # Aplicando a operação de inversão (negativo)
    imagem_negativa = cv2.bitwise_not(imagem_brilho)

    # Aplicando a operação de desfoque
    imagem_desfocada = cv2.GaussianBlur(imagem_negativa, (21, 21), sigmaX=0, sigmaY=0)

    # Invertendo a imagem novamente
    imagem_desenho = cv2.divide(imagem_brilho, 255 - imagem_desfocada, scale=256.0)

    return imagem_desenho

# Carregar a imagem
imagem_original = cv2.imread('/mnt/d/Workspace/5cfbd596-42fd-417f-bba4-2ce11e99fd7c.png')

# Controlar o nível de brilho (valores < 1.0 reduzem o brilho, valores > 1.0 aumentam o brilho)
nivel_de_brilho = 1.5

# Transformar a imagem em desenho com o nível de brilho especificado
imagem_desenho = transformar_para_desenho(imagem_original, brilho=nivel_de_brilho)

# Salvar o resultado em um novo arquivo
caminho_resultado = '/mnt/d/Workspace/5cfbd596-42fd-417f-bba4-2ce11e99fd7c_2.png'
cv2.imwrite(caminho_resultado, imagem_desenho)

# Exibir a imagem original e o desenho lado a lado
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagem_original, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')

plt.subplot(1, 2, 2)
plt.imshow(imagem_desenho, cmap='gray')
plt.title('Desenho')

plt.show()
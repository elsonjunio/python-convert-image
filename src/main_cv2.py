import cv2
import numpy as np

def convert_to_sketch(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)

    # Converter a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar um desfoque gaussiano para reduzir o ruído
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Detectar as bordas na imagem usando o método Canny
    edges = cv2.Canny(blurred_image, 30, 150)

    # Inverter as cores (preto para branco e branco para preto)
    edges_inv = cv2.bitwise_not(edges)

    # Criar uma imagem em branco com o mesmo tamanho da imagem original
    sketch = np.zeros_like(gray_image)

    # Combinação da imagem original com as bordas invertidas
    cv2.bitwise_and(blurred_image, blurred_image, dst=sketch, mask=edges_inv)

    cv2.imwrite('/mnt/d/Workspace/5cfbd596-42fd-417f-bba4-2ce11e99fd7c_3.png', sketch)
    
    # Exibir a imagem original e a imagem em desenho
    cv2.imshow('Original Image', image)
    cv2.imshow('Sketch', sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

# Substitua 'caminho/para/sua/imagem.jpg' pelo caminho da sua própria imagem
convert_to_sketch('/mnt/d/Workspace/5cfbd596-42fd-417f-bba4-2ce11e99fd7c.png')
import cv2


def photo_to_draw(input: str, output: str, bright=1.0, show=False):

    # Carregar a image
    image = cv2.imread(input)

    # Convertendo a image para escala de cinza
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Ajustar o brilho da image
    # Controlar o nível de brilho (valores < 1.0 reduzem o brilho, valores > 1.0 aumentam o brilho)
    image_brilho = cv2.add(image_gray, bright)

    # Aplicando a operação de inversão (negativo)
    image_negative = cv2.bitwise_not(image_brilho)

    # Aplicando a operação de desfoque
    image_blur = cv2.GaussianBlur(image_negative, (21, 21), sigmaX=0, sigmaY=0)

    # Invertendo a image novamente
    image_draw = cv2.divide(image_brilho, 255 - image_blur, scale=256.0)

    # Salvar o resultado em um novo arquivo
    cv2.imwrite(output, image_draw)

    if show:
        print('PRESS ENTER IN THE WINDOW TO EXIT')
        cv2.imshow('Original Image', image)
        cv2.imshow('Sketch', image_draw)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

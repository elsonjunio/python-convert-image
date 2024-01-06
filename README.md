# photo2drawing


O pacote photo2drawing é uma ferramenta Python que permite converter fotos em desenhos. Faço uso deste pacote para preparar fotos para uso em CNC Laser.

## Instalação

Certifique-se de ter o Python > 3.10 e o Poetry instalados em seu ambiente. Em seguida, execute o seguinte comando para instalar o pacote:

```bash
git clone https://github.com/elsonjunio/python-convert-image.git
cd python-convert-image
poetry build
pip install dist/photo2drawing-0.1.0.tar.gz
```

## Uso

Após a instalação, você pode usar o pacote como um script de linha de comando. Execute o seguinte comando para converter uma foto em desenho:

```bash
python -m photo2drawing -i example.jpg -o example.png -s
```

```bash
python -m photo2drawing -h
usage: __main__.py [-h] -o OUTPUT -i INPUT [-d] [-s] [-b BRIGHT]

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output Filename
  -i INPUT, --input INPUT
                        Input Filename
  -d, --draw            Uses draw method
  -s, --show            Show images
  -b BRIGHT, --bright BRIGHT Image brightness default=1.0
```

## Dependências

O projeto usa OpenCV para processamento de imagem.

As dependências estão listadas no arquivo pyproject.toml e são gerenciadas pelo Poetry.


## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.
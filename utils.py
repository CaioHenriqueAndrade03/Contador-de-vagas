import cv2
def criarRetangulo(imagem, ondeComeca, ondeTermina, cor, grossura):
             cv2.rectangle(imagem, ondeComeca, ondeTermina, cor, grossura)
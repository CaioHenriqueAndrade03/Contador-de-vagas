import cv2
import pickle
from utils import criarRetangulo

img = cv2.imread('src/estacionamento.png')

vagas = [ ]

for x in range(69):
          vaga = cv2.selectROI('vagas',img, False)
          cv2.destroyWindow('vagas')
          vagas.append((vaga))

          for x, y, w, h in vagas:
                   criarRetangulo(img,(x,y),(x+w,y+h),(255,0,0),2)

with open('vagas.pkl', 'wb') as arquivo:
          pickle.dump(vagas, arquivo)
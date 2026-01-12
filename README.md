# Detector de Vagas de Estacionamento com OpenCV

Projeto simples de **visão computacional** que identifica vagas livres e ocupadas em um estacionamento a partir de vídeo, usando **Python + OpenCV**.

##  Funcionalidades

* Marcação manual das vagas (uma única vez)
* Detecção automática de vagas livres/ocupadas
* Contador de vagas disponíveis em tempo real
* Visualização com retângulos coloridos:

  * 🟢 Verde: vaga livre
  * 🔴 Vermelho: vaga ocupada

## Tecnologias utilizadas

* Python 3
* OpenCV
* NumPy

##  Estrutura do projeto

```
├── capturarVagas.py      # Script para marcar manualmente as vagas
├── contadorVagas.py     # Script principal de detecção
├── utils.py              # Funções auxiliares
├── vagas.pkl             # Arquivo com as coordenadas das vagas
└── src/
    ├── video.mp4         # Vídeo do estacionamento
    └── estacionamento.png# Imagem base para marcar vagas
```


## Como usar

### Marcar as vagas

Execute e selecione manualmente cada vaga no estacionamento:

```bash
python capturarVagas.py
```
<img width="945" height="651" alt="image" src="https://github.com/user-attachments/assets/821aa287-4921-4baa-b71d-08401185c826" />


* salva automaticamente as vagas no arquivo `vagas.pkl`

### Rodar o detector

Depois de marcar as vagas:

```bash
python contadorVagas.py
```
<img width="1074" height="696" alt="image" src="https://github.com/user-attachments/assets/69676c39-0474-4420-b7b6-611ed2bac1b1" />


* O vídeo será processado
* As vagas serão analisadas frame a frame
* O contador de vagas livres aparecerá na tela

## Como funciona (resumo técnico)

* Converte o vídeo original para cinza

- Aplica **threshold adaptativo**
- Usa **blur + dilatação** para reduzir ruído
- Conta pixels brancos dentro de cada vaga
- Define se a vaga está livre ou ocupada com base em um limiar

## Observações

* O valor que define se uma vaga ta cheia ou não é `1000` podendo ser ajustado a cada situação
* O número de vagas está fixo em 69 por que no video usado, so temos 69 vagas

## Objetivo do projeto

Projeto educacional para praticar:

* Visão computacional
* Processamento de imagens
* OpenCV na prática

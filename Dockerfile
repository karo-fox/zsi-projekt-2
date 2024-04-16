# Korzystamy z obrazu bazującym na Linux Alpine, z przygotowanym środowiskiem Python
FROM python:3.10.14-alpine3.18
# Ustawiamy katalog roboczy na /usr/src/app
WORKDIR /usr/src/app

# Uruchamiamy komendę instalującą bash
RUN apk add --no-cache bash

# Kopiujemy plik z zapisanymi zależnościami naszej aplikacji do katalogu roboczego
COPY requirements.txt ./
# Uruchamiamy polecenie instalujące zależności naszej aplikacji
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy całą resztę naszego projektu do katalogu roboczego
COPY . .

# Udostępniamy port 5000
EXPOSE 5000

# Uruchamiamy skrypt start.sh, służący do skonfigurowania i uruchomienia aplikacji
CMD ./start.sh
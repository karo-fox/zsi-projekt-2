#!/bin/bash

help() {
    echo """Składnia: run.sh [opcje]

    Dla każdego pliku w katalogu ./in wykonuje zadanie algorytmiczne, którego wynik zapisuje w katalogu ./out

    Opcje:
     -r, --report   po ukończeniu zadania utwórz raport html z wynikami
     -b, --backup   dodaj backup ostatniego wygenerowanego raportu 
                    z obecnym timestampem
     -h, --help     wyświetla pomoc"""
}

wd=$(dirname $0);

files=()

for file in ./in/*; do
    file_number=${file#./in/in}
    file_name=./out/out$file_number
    games_counter=$(cat $file)
    python -m main $games_counter > $file_name
    files+=($file_name)
done

while [[ $# -gt 0 ]]; do
    case "$1" in
        -r | --report) python -m html_report ${files[*]} > ./report/index.html; firefox ./report/index.html ;;
        -b | --backup) python -m backup ;;
        -h | --help) help ;;
    esac
    shift
done



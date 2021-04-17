"""First assignment
"""
# -*- coding: iso-8859-15 -*-
import argparse
import logging

logging.basicConfig(level=logging.INFO)

def process(file_path): # c'è la virgola in modo che se non stampa il messaggio lui non lo formatta
    logging.info("Reading input file %s...", file_path)

if __name__ == '__main__':        # cose eseguite solo quando il file viene eseguito direttamente
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help='Path to the input file')   #path del file di input
    args = parser.parse_args()

    process(args.infile)

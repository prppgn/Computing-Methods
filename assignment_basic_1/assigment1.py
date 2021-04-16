# -*- coding: iso-8859-15 -*-
import argparse
import logging

logging.basicConfig(level=logging.WARNING)

def process(file_path):
  logging.warning("Reading input file %s...", file_path)  #c'è la virgola in modo che se il messaggio non viene stampato lui non lo formatta e risparmia tempo

if __name__ == '__main__':        #cose eseguite solo quando il file viene eseguito direttamente
  parser = argparse.ArgumentParser()
  parser.add_argument('infile', type=str, help='Path to the input file')   #stringa con il path del file di input
  args = parser.parse_args()


  process(args.infile)

"""First assignment
"""
# -*- coding: iso-8859-15 -*-
import argparse
import logging
import time
import string

logging.basicConfig(level=logging.INFO)

def process(file_path): # c'è la virgola in modo che se non stampa il messaggio lui non lo formatta
    """ Reads a text file and compile the letter statistics"""
    start_time = time.time()

    logging.info("Reading input file %s...", file_path)
    with open(file_path) as input_file:
    # with = context manager, il file viene chiuso appena finisce il blocco di codice del with
    # vedere bene come funziona with e il concetto di context management
        text = input_file.read()
    num_chars = len(text)
    logging.info("Done, %d characters found", num_chars)
    # il professore trova 1214387 caratteri
    # io ne trovo 1214416, qualcosa non va

    #char_dict = {chr(x): 0 for x in range(ord('a'), ord('z') + 1)}
    # ord() da il numero d'ordine di un carattere (vedi tabella ASCII)
    # chr(x) da il carattere di numero d'ordine x

    char_dict = {ch: 0 for ch in string.ascii_lowercase}
    # piu pythonico del precedente
    for ch in text:
        # i 2 modi seguenti sono ugualmente pythonici
        ch=ch.lower()
        if ch in char_dict:
            char_dict[ch] += 1

        # try: # se il valore e' nelle chiavi gia' inserite, incrementa il valore
        #     char_dict[ch.lower()] += 1
        # except KeyError: # altrimenti non fa fiente
        #     pass

    elapsed_time = time.time() - start_time
    logging.info("Done in %.3f seconds", elapsed_time)
    num_letters = sum(char_dict.values())
    print(num_letters)
    for ch, num in char_dict.items():
        print(f"{ch} ->{num / num_letters:.3%}")  #il formato % moltiplica per 100 e da la percentuale
    print(char_dict)


if __name__ == '__main__':        # cose eseguite solo quando il file viene eseguito direttamente
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help='Path to the input file')   #path del file di input
    args = parser.parse_args()

    process(args.infile)

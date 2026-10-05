def leggi_studenti(nome_file):
    """Legge studenti.csv e restituisce una lista di dizionari."""
    studenti = []
    with open(nome_file, "r", encoding="utf-8") as f:
        # Uso next() per saltare la prima riga perché
        # è quella di intestazione
        next(f) 
        for riga in f:
            riga = riga.strip("\n")
            if len(riga) <= 0:
                continue
            campi = riga.split(",")
            studente = {
                "id": int(campi[0]),
                "cognome": campi[1],
                "nome": campi[2],
                "classe": campi[3],
                "media": float(campi[4])
            }
            studenti.append(studente)
        return studenti
            
def leggi_richieste(nome_file):
    """Legge richieste.txt e restituisce (lista_id, cognome, classe)."""
    # 1. Apri il file e leggi le tre righe (es. f.readlines()).
    # 2. Per ogni riga ricordati di fare strip().
    # 3. Riga 1: e' una stringa tipo "103,107,115,110".
    #    - fai split(",") e converti OGNI elemento in int
    #      (ti servira' una list comprehension o un ciclo for).
    # 4. Riga 2: e' il cognome (stringa, la lasci cosi').
    # 5. Riga 3: e' la classe (stringa).
    # 6. Restituisci le tre informazioni insieme: return ids, cognome, classe
    with open(nome_file, "r", encoding="utf-8") as f:
        pass


def cerca_per_id(studenti, id_cercato):
    """Restituisce il dizionario dello studente con quell'ID, oppure None."""
    # 1. Scorri la lista degli studenti.
    # 2. Se studente["id"] == id_cercato -> restituiscilo subito (return).
    # 3. Se il ciclo finisce senza trovare nulla -> return None.
    pass


def cerca_per_cognome(studenti, cognome):
    """Restituisce la lista degli studenti con quel cognome."""
    # 1. Crea una lista vuota per i risultati.
    # 2. Il confronto NON deve distinguere maiuscole/minuscole:
    #    confronta studente["cognome"].lower() con cognome.lower()
    # 3. Aggiungi alla lista i dizionari che corrispondono.
    # 4. Restituisci la lista (puo' essere vuota: la gestirai nel main).
    pass


def media_classe(studenti, classe):
    """Restituisce (media, numero_studenti) della classe indicata."""
    # 1. Usa DUE accumulatori: somma = 0 e conteggio = 0.
    # 2. Scorri gli studenti: se studente["classe"] == classe
    #    -> somma += studente["media"] e conteggio += 1
    #    (se vuoi essere tollerante, confronta anche qui con .upper()).
    # 3. Dividi SOLO dopo aver controllato che conteggio != 0.
    # 4. Se conteggio == 0 restituisci (None, 0) (o un altro modo a tua scelta
    #    per segnalare "classe vuota").
    # 5. Altrimenti restituisci (somma / conteggio, conteggio).
    pass


def stampa_studente(studente):
    """Stampa un record su una sola riga: ID cognome nome classe media."""
    # Usa print() con una f-string, campi separati da UNO spazio.
    # Esempio di formato atteso: 103 Ferrero Sara 5A 8.5
    # Questa funzione si occupa SOLO di stampare, nessun'altra logica.
    pass


def main():
    studenti = leggi_studenti("studenti.csv")
    #ids, cognome, classe = leggi_richieste("richieste.txt")

    # --- Ricerca per ID ---
    # print("--- Ricerca per ID ---")
    # Per ogni id in ids (nell'ORDINE del file):
    #   - chiama cerca_per_id
    #   - se il risultato e' None -> print(f"ID {id} non trovato")
    #   - altrimenti -> stampa_studente(risultato)

    # --- Ricerca per cognome ---
    # Stampa una riga vuota, poi l'intestazione:
    #   --- Ricerca per cognome: <cognome> ---
    # Chiama cerca_per_cognome:
    #   - se la lista e' vuota -> "Nessuno studente trovato"
    #   - altrimenti stampa_studente per ognuno

    # --- Media della classe ---
    # Stampa una riga vuota, poi l'intestazione:
    #   --- Media della classe <classe> ---
    # Chiama media_classe:
    #   - se il conteggio e' 0 -> "Nessuno studente nella classe <classe>"
    #   - altrimenti stampa:
    #       Studenti considerati: <n>
    #       Media: <media con 2 decimali>   (suggerimento: f"{media:.2f}")
    pass


if __name__ == "__main__":
    main()
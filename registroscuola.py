def leggi_studenti(nome_file: str) -> list[dict]:
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


def leggi_richieste(nome_file: str) -> tuple[list[int], str, str]:
    """Legge richieste.txt e restituisce (lista_id, cognome, classe)."""
    with open(nome_file, "r", encoding="utf-8") as f:
        righe = f.readlines()

        elementi = []
        for elemento in righe[0].strip().split(","):
            elementi.append(int(elemento))
            
        cognomi = righe[1].strip()
        classi = righe[2].strip()

    return elementi, cognomi, classi


def cerca_per_id(studenti: list[dict], id_cercato: int) -> dict | None:
    """Restituisce il dizionario dello studente con quell'ID, oppure None."""
    for studente in studenti:
        if studente["id"] == id_cercato:
            return studente
    return None


def cerca_per_cognome(studenti: list[dict], cognome: str) -> list[dict]:
    """Restituisce la lista degli studenti con quel cognome."""
    risultati = []

    for studente in studenti:
        if studente["cognome"].lower() == cognome.lower():
            risultati.append(studente)

    return risultati


def media_classe(studenti: list[dict], classe: str) -> tuple[float | None, int]:
    """Restituisce (media, numero_studenti) della classe indicata."""
    somma = 0
    conteggio = 0

    for studente in studenti:
        if studente["classe"].upper() == classe.upper():
            somma += studente["media"]
            conteggio += 1

    if conteggio == 0:
        return None, 0

    return somma / conteggio, conteggio


def stampa_studente(studente: dict):
    """Stampa un record su una sola riga: ID cognome nome classe media."""
    # Usa print() con una f-string, campi separati da UNO spazio.
    # Esempio di formato atteso: 103 Ferrero Sara 5A 8.5
    # Questa funzione si occupa SOLO di stampare, nessun'altra logica.
    print(f"{studente['id']} {studente['cognome']} {studente['nome']} {studente['classe']} {studente['media']}")


def main():
    studenti = leggi_studenti("studenti.csv")
    ids, cognome, classe = leggi_richieste("richieste.txt")

    print("--- Ricerca per ID ---")
    for id in ids:
        studente = cerca_per_id(studenti, id)
        if studente is None:
            print(f"Studente con ID {id} non trovato")
        else:
            stampa_studente(studente)

    print("")

    print(f"--- Ricerca per cognome: {cognome} ---")
    cognomi_studenti = cerca_per_cognome(studenti, cognome)
    if len(cognomi_studenti) == 0:
        print("Nessuno studente trovato")
    else:
        for studente in cognomi_studenti:
            stampa_studente(studente)

    print("")

    print(f"--- Media della classe {classe} ---")
    media, conteggio = media_classe(studenti, classe)
    if conteggio == 0:
        print(f"Nessuno studente nella classe {classe}")
    else:
        print(f"Studenti considerati: {conteggio}")
        print(f"Media: {media:.2f}")

if __name__ == "__main__":
    main()
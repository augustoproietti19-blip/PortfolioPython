def minuti_da_inizio_mese(giorno, ora, minuto):
    return (giorno - 1) * 24 * 60 + ora * 60 + minuto # trasformare (data,ora,minuto) in un intero corrispondente al numero di minuti trascorsi dall'inizio del mese


def ottieniDatiTelefonate(telefonate): #implemento la funzione

    lista_telefonate = [] #tuple

    with open(telefonate, "r") as file:

        next(file) # salta l'intestazione

        for riga in file:

            riga = riga.strip() #salta righe vuote e contenenti cancelletto

            if riga == "":
                continue

            if riga.startswith("#"):
                continue

            campi = riga.split(";") # inserisco il separatore

            chiamante = int(campi[0]) #trasformo i dati in numeri interi
            destinatario = int(campi[1])

            cella_chiamante = int(campi[2])
            cella_destinatario = int(campi[3])

            inizio = campi[4].split(":")
            fine = campi[5].split(":")

            giorno_i = int(inizio[0])
            ora_i = int(inizio[1])
            minuto_i = int(inizio[2])

            giorno_f = int(fine[0])
            ora_f = int(fine[1])
            minuto_f = int(fine[2])

            if chiamante == destinatario: #controlli
                continue

            if giorno_i < 1 or giorno_i > 31:
                continue

            if giorno_f < 1 or giorno_f > 31:
                continue

            if ora_i < 0 or ora_i > 23:
                continue

            if ora_f < 0 or ora_f > 23:
                continue

            if minuto_i < 0 or minuto_i > 59:
                continue

            if minuto_f < 0 or minuto_f > 59:
                continue

            minuti_inizio = minuti_da_inizio_mese(
                giorno_i,
                ora_i,
                minuto_i
            )

            minuti_fine = minuti_da_inizio_mese(
                giorno_f,
                ora_f,
                minuto_f
            )

            if minuti_inizio > minuti_fine:
                continue

            durata = minuti_fine - minuti_inizio + 1

            if durata > 600:
                continue

            telefonata = ( #tupla da restituire
                chiamante,
                destinatario,
                cella_chiamante,
                cella_destinatario,
                durata
            )

            lista_telefonate.append(telefonata)

    return lista_telefonate
preis_erwachsene = 5.0
preis_kinder = 2.5
preis_jugend = 3.5
preis_premium = 3.0
preis_basis = 4.0

while True:
    print(" ### Tarifauskunftsrechner Museum XXX ### ")
    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())
    print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")

    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(" Preis: ", preis_kinder, " Euro ")
    if alter_gast < 18:
        print(" ### Eintritt Jugendliche ### ")
        print(" Preis: ", preis_jugend, " Euro ")
    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste. ")
        antwort_rabatt = input();
        if antwort_rabatt == "p":
            print(" ### Eintritt Premium-Mitglied ### ")
            print(" Preis: ", preis_premium, " Euro ")
        elif antwort_rabatt == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            print(" Preis: ", preis_basis, " Euro ")
        else:
            print(" ### Eintritt Erwachsene (voller Preis) ### ")
            print(" Preis: ", preis_erwachsene, " Euro")

    print("Viel Spaß!")

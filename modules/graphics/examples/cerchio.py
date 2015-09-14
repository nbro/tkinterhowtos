from graphics import *
import math


def start():
    finestra = GraphWin("Exercizio 1", 300, 300)
    
    linea_superiore = Line(Point(0, 50), Point(200, 50))
    linea_superiore.draw(finestra)  # passi dove vuoi disegnare la linea, cioè nella "finestra"

    raggioCerchio = 10
    cerchio = Circle(Point(40, 260), raggioCerchio)
    cerchio.setFill("grey")
    cerchio.draw(finestra)
    

    # per 20 volte, dimuinisci differenzaY di 10
    # e aggiorna la posizione del cerchio
    for i in range(20):
        
        primoPuntoDelCerchio = cerchio.getP1()

        # serve solo a far vedere le nuove coordinate
        print(primoPuntoDelCerchio.getX(), primoPuntoDelCerchio.getY())

        # per ora la differenza in pixels da muovere sull asse Y è 0
        differenzaY = 0

        # se il cerchio non è ancora arrivato alla linea
        # allora aggiorna la "differenzaY"
        if primoPuntoDelCerchio.getY() > linea_superiore.getP1().getY():
            differenzaY = differenzaY - 10  # diminuisci di 10 pixel

        # per ora la distanza sull asse X non cambia
        # quindi gli passo 0 come differenza
        cerchio.move(0, differenzaY)


    # visto che la posizione iniziale del cerchio è x=30
    # e la linea è lunga 200 partendo da zero,
    # allora mancano 170 fino alla fine della linea
    # se vogliamo muovere fino alla fine della linea partendo da 30
    # con passi da 10, allora abbiamo bisogno più o meno 17 cicli
    for i in range(17):

        # ora controlliamo dove è il secondo punto del cerchio
        secondoPuntoDelCerchio = cerchio.getP2()

        # fa il print delle coordinate...
        print(secondoPuntoDelCerchio.getX(), secondoPuntoDelCerchio.getY())

        differenzaX = 0
        
        if secondoPuntoDelCerchio.getX() < linea_superiore.getP2().getX():
            differenzaX = differenzaX + 10

        # non si muove verticalmente, ma solo orizzontalmente
        cerchio.move(differenzaX, 0)



    # aspetta finché non fai click
    # dopo disegna la linea in basso
    # e fa cadere il cerchio
    finestra.getMouse()  

    # disegna la linea in basso
    linea_inferiore = Line(Point(100, 250), Point(200, 250))
    linea_inferiore.draw(finestra)


    # per far cadere il cerchio,
    # abbiamo bisogno di un altro for loop
    # è simile al primo for loop,
    # ma ora la differenzaY viene aumentata
    # per fare andare il cerchio giù
    
    for i in range(20):
        # controlliamo dove è il secondo punto del cerchio
        # quello più in basso
        secondoPuntoDelCerchio = cerchio.getP2()

                # fa il print delle coordinate...
        print(secondoPuntoDelCerchio.getX(), secondoPuntoDelCerchio.getY())

        differenzaY = 0

        # il confronto è ora con la linea inferiore
        if secondoPuntoDelCerchio.getY() < linea_inferiore.getP2().getY():
            differenzaY = differenzaY + 10

        # non si muove orizzontalmente, ma solo verticalmente 
        cerchio.move(0, differenzaY)


    # per calcolare l'area del cerchio: raggio^2 * pi

    areaCerchio = (raggioCerchio**2) * math.pi

    # per far vedere l'area del cerchio uso un Text

    text = Text(Point(150, 100), "Area cerchio: " + str(areaCerchio))
    text.draw(finestra)

    finestra.getMouse()
    finestra.close()

start()

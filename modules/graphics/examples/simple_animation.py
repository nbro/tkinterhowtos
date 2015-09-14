from graphics import *


def start():
    finestra = GraphWin("Exercizio 1", 300, 300)
    
    linea_superiore = Line(Point(0, 50), Point(200, 50))
    linea_superiore.draw(finestra)  # passi dove vuoi disegnare la linea, cioè nella "finestra"

    #cerchio = Circle(Point(40, 260), 10)
    #cerchio.setFill("grey")
    #cerchio.draw(finestra)
    
    quadrato = Rectangle(Point(30, 250), Point(50, 270))
    quadrato.setFill("grey")
    quadrato.draw(finestra) # disegna il quadrato nella "finestra"


    # per 20 volte, dimuinisci differenzaY di 10
    # e aggiorna la posizione del quadrato
    for i in range(20):
        
        puntoAltoDelQuadrato = quadrato.getP1()

        # serve solo a far vedere le nuove coordinate
        print(puntoAltoDelQuadrato.getX(), puntoAltoDelQuadrato.getY())

        # per ora la differenza in pixels da muovere sull asse Y è 0
        differenzaY = 0

        # se il quadrato non è ancora arrivato alla linea
        # allora aggiorna la "differenzaY"
        if puntoAltoDelQuadrato.getY() > linea_superiore.getP1().getY():
            differenzaY = differenzaY - 10  # diminuisci di 10 pixel

        # per ora la distanza sull asse X non cambia
        # quindi gli passo 0 come differenza
        quadrato.move(0, differenzaY)


    # visto che la posizione iniziale del quadrato è x=30
    # e la linea è lunga 200 partendo da zero,
    # allora mancano 170 fino alla fine della linea
    # se vogliamo muovere fino alla fine della linea partendo da 30
    # con passi da 10, allora abbiamo bisogno più o meno 17 cicli
    for i in range(17):

        # ora controlliamo dove è il secondo punto del quadrato
        secondoPuntoDelQuadrato = quadrato.getP2()

        # fa il print delle coordinate...
        print(secondoPuntoDelQuadrato.getX(), secondoPuntoDelQuadrato.getY())

        differenzaX = 0
        
        if secondoPuntoDelQuadrato.getX() < linea_superiore.getP2().getX():
            differenzaX = differenzaX + 10

        # non si muove verticalmente, ma solo orizzontalmente
        quadrato.move(differenzaX, 0)



    # aspetta finché non fai click
    # dopo disegna la linea in basso
    # e fa cadere il quadrato
    finestra.getMouse()  

    # disegna la linea in basso
    linea_inferiore = Line(Point(100, 250), Point(200, 250))
    linea_inferiore.draw(finestra)


    # per far cadere il quadrato,
    # abbiamo bisogno di un altro for loop
    # è simile al primo for loop,
    # ma ora la differenzaY viene aumentata
    # per fare andare il quadrato giù
    
    for i in range(20):
        # controlliamo dove è il secondo punto del quadrato
        # quello più in basso
        secondoPuntoDelQuadrato = quadrato.getP2()

                # fa il print delle coordinate...
        print(secondoPuntoDelQuadrato.getX(), secondoPuntoDelQuadrato.getY())

        differenzaY = 0

        # il confronto è ora con la linea inferiore
        if secondoPuntoDelQuadrato.getY() < linea_inferiore.getP2().getY():
            differenzaY = differenzaY + 10

        # non si muove orizzontalmente, ma solo verticalmente 
        quadrato.move(0, differenzaY)

    finestra.getMouse()
    finestra.close()

start()

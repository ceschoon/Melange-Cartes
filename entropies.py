import numpy

def entropie_1(N,melange,p,tps):

    """
    Entropie à 1 position
    
    Paramètres:
    -----------
    1: Taille du paquet à mélanger
    2: Procédure de mélange
    3: Position initiale de la carte connue
    4: Nombre de simulations par configuration finale
    
    Renvoie:
    --------
    1: L'entropie à la position donnée
    2: La densité de probabilité sur les configurations finales
    """
    
    M = int(N*tps) # nombre de simulations pour effectuer l'histogramme des configurations observées
    
    paquet_initial = numpy.arange(1,N+1)
    histogramme = numpy.zeros(N)
    
    for i in range(M):
        
        paquet_melange = melange(paquet_initial)
        histogramme[numpy.where(paquet_melange==p)] += 1
        
    probas = histogramme/M
    log_probas = numpy.zeros(len(probas))

    for i in range(len(probas)):
        if probas[i]!=0:
            log_probas[i] = numpy.log(probas[i])

    entropie = - numpy.sum(probas*log_probas)
    
    return (entropie,probas)
    
    
def entropie_2(N,melange,p1,p2,tps):

    """
    Entropie à 2 positions
    
    Paramètres:
    -----------
    1: Taille du paquet à mélanger
    2: Procédure de mélange
    3: Position initiale de la carte connue #1
    4: Position initiale de la carte connue #2
    5: Nombre de simulations par configuration finale
    
    Renvoie:
    --------
    1: L'entropie au couple de positions donné
    2: La densité de probabilité sur les configurations finales
    """
    
    M = int(N*(N-1)*tps) # nombre de simulations pour effectuer l'histogramme des configurations observées
    
    paquet_initial = numpy.arange(1,N+1)
    histogramme = numpy.zeros((N,N))
    
    for i in range(M):
        
        # indicateur de progression
        #if (i%(N*(N-1)*10)==0):
        #    print(i/(N*(N-1)),"/100")
            
        paquet_melange = melange(paquet_initial)
        histogramme[numpy.where(paquet_melange==p1),numpy.where(paquet_melange==p2)] += 1
        
    probas = histogramme/M
    log_probas = numpy.zeros((len(probas[:,0]),len(probas[0,:])))

    for i in range(len(probas[:,0])):
        for j in range(len(probas[0,:])):
            
            if probas[i][j]!=0:
                log_probas[i][j] = numpy.log(probas[i][j])

    entropie = - numpy.sum(probas*log_probas)
        
    return (entropie,probas)
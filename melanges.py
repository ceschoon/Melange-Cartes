import numpy

def melange_1(paquet,n,tmin,tmax):
    
    """
    Fonction de mélange d'un paquet de cartes à la manière "haut-bas"

    Paramètres
    ----------
    1: Le paquet à mélanger, sous forme d'un vecteur numpy.array d'entiers de 1 à #cartes
    2: Nombre de mélanges à effectuer, un entier
    3: Taille minimale des petits paquets de cartes à faire passer du paquet du dessus (ancien) 
       au paquet du dessous (nouveau). Ce nombre sera tiré uniformément entre cette taille minimale et la 
    4: taille maximale utilisée.

    Renvoie:
    --------
    Le paquet mélangé, toujours sous forme d'un vecteur numpy.array d'entiers de 1 à #cartes
    """

    N = len(paquet)
    paquet_nouv = numpy.array([])
    paquet_reste = paquet

    for i in range(n):
        
        t = int(numpy.random.uniform(tmin,tmax+1))
        paquet_nouv = paquet_reste[:t]
        paquet_reste = paquet_reste[t:]
        
        while(len(paquet_reste)>tmax):
            
            t = int(numpy.random.uniform(tmin,tmax+1))
            paquet_nouv = numpy.concatenate((paquet_reste[:t],paquet_nouv))
            paquet_reste = paquet_reste[t:]
            
        paquet_nouv = numpy.concatenate((paquet_reste,paquet_nouv))
        paquet_reste = paquet_nouv
        
    return paquet_nouv
    
   
def melange_2(paquet,n,tmax,p):
    
    """
    Fonction de mélange d'un paquet de cartes à la manière "alternée" (riffle shuffle)

    Paramètres
    ----------
    1: Le paquet à mélanger, sous forme d'un vecteur numpy.array d'entiers de 1 à #cartes
    2: Nombre de mélanges à effectuer, un entier
    3: Taille maximale des petits paquets de cartes qui s'alternent durant le mélange.
       Ce nombre sera tiré selon une binomiale entre 1 et la taille maximale indiquée avec la
    4: Probabilité pour la binomiale tirant la taille des petits paquets
    
    Renvoie:
    --------
    Le paquet mélangé, toujours sous forme d'un vecteur numpy.array d'entiers de 1 à #cartes
    """

    N = len(paquet)
    paquet_ancien = paquet

    for i in range(n):
        
        paquet_nouv = numpy.array([])
        
        m = int(numpy.random.uniform(N/2-N/12,N/2+N/12+1))
        if(numpy.random.uniform(0,1)>0.5):
            paquet_moitie_1 = paquet_ancien[:m]
            paquet_moitie_2 = paquet_ancien[m:]
        else:
            paquet_moitie_2 = paquet_ancien[:m]
            paquet_moitie_1 = paquet_ancien[m:]
        
        while(len(paquet_moitie_1)>tmax and len(paquet_moitie_2)>tmax):
            
            t1 = int(numpy.random.binomial(tmax,p))+1
            t2 = int(numpy.random.binomial(tmax,p))+1
            paquet_nouv = numpy.concatenate((paquet_moitie_2[-t2:],paquet_moitie_1[-t1:],paquet_nouv))
            paquet_moitie_1 = paquet_moitie_1[:-t1]
            paquet_moitie_2 = paquet_moitie_2[:-t2]
            
        paquet_nouv = numpy.concatenate((paquet_moitie_2,paquet_moitie_1,paquet_nouv))
        paquet_ancien = paquet_nouv
                
    return paquet_nouv

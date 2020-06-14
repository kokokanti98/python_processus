import threading
from threading import Thread
from random import randint
import os, time, multiprocessing
from multiprocessing import Pool
from multiprocessing import Process
 
# Définition de notre classe fichier
class fichier_manipulation: 
    """Voila notre classe FICHIERMANIP avec ses donnees:
    -nom_fichier"""
    def __init__(self,nom): # Notre méthode constructeur
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self.nom_fichier = nom

    #fonction pour ecrire sur la meme ligne dans un fichier
    def ecrire_meme_ligne_fichier(self,ecrire):
        fichier = open(self.nom_fichier, "a")
        fichier.write("\t"+ecrire)
        fichier.close()

    #fonction pour ecrire a la ligne dans un fichier
    def ecrire_a_la_ligne_fichier(self,ecrire):
        fichier = open(self.nom_fichier, "a")
        fichier.write("\n"+ecrire)
        fichier.close()

    #fonction pour lire et afficher les truc ecrit dans un fichier
    def lecture_affichage_fichier(self):
        fichier = open(self.nom_fichier, "r")
        print (fichier.read())
        fichier.close()

    #fonction pour ecrire dans un fichier supprimer avant d'ecrire grace a w
    def suppr_ecriture_fichier(self,ecrire):
        fichier = open(self.nom_fichier, "w")
        if(fichier):
            fichier.write(ecrire)
            fichier.close()
        else :
              ecriture_si_existepas_fichier(self.nom_fichier);
              fichier.close()

    #fonction pour effacer le truc dans un fichier
    def effacer_texte_fichier(self):
        fichier = open(self.nom_fichier, "w").close()

    #fonction pour ecrire dans un fichier si ca n'esxite te pas
    def ecriture_si_existepas_fichier(self,ecrire):
        fichier = open(self.nom_fichier, "a")
        fichier.write(ecrire)
        fichier.close()
 
class MyThread(Thread):
 
    def __init__(self, repetition, delay):
        ''' Constructor. '''
        Thread.__init__(self)
        self.lock = threading.Lock()
        self.semaphore = threading.BoundedSemaphore()
        self.val = repetition
        self.secondsToSleep = delay
        #self.var = var_multiplication
 
 
    def run(self):
         for i in range(1, self.val):
             #nom = input("entrez le nom_du_fichier.extension a maninupuler:")
             mon_fichier = fichier_manipulation("file.txt");
             self.lock.acquire()
             try:
                  print('Index %d -- We see in file.txt in thread %s\n' % (i,self.getName()))
                  mon_fichier.lecture_affichage_fichier();
             finally:
                  self.lock.release()
             mon_fichier1 = fichier_manipulation("fichier.txt");
             self.semaphore.acquire()
             try:
                  print('Index %d -- We see in file.txt in thread %s\n' % (i,self.getName()))
                  mon_fichier1.lecture_affichage_fichier();
             finally:
                  self.semaphore.release()
             print('%s sleeping for %d seconds...' % (self.getName(), self.secondsToSleep))
             time.sleep(self.secondsToSleep)
         print('Process %s is  Finished' % (self.getName()))

    #def print_result(self):
         #print('la variable du thread %s est : %d\n' % (self.getName(), self.var))

class Myprocess(Process):
    def __init__(self,process_number,repetition,p_time,nombre_multiplie,fichier):
        super(Myprocess, self).__init__()
        self.repeat = repetition
        self.delay_time = p_time
        self.number = nombre_multiplie
        self.process_number = process_number
        self.file = fichier
        self.emeteur = emeteur(self.process_number)
        self.recepteur = recepteur(self.process_number)
    def run(self):
        print('Process number:',self.process_number)
        print('parent process:', os.getppid())
        print('process id:', os.getpid())           
        print('Emeteur:', self.emeteur)
        print('Recepteur:',self.recepteur)
        for idx in range (self.repeat):
            print(str(os.getpid()) + " Working for then sleep for",self.delay_time) 
            self.number = self.number+1;
            time.sleep(self.delay_time)
        if(self.recepteur==False and self.emeteur==True):
            self.file.suppr_ecriture_fichier("Nombre final dans Process %d est %d" %(self.process_number,self.number))
        elif(self.recepteur==True and self.emeteur==True):
            self.file.lecture_affichage_fichier()
            self.file.ecrire_a_la_ligne_fichier("Nombre final dans Process %d est %d" %(self.process_number,self.number))           
        else:
            self.file.lecture_affichage_fichier()
        print ("Process ",self.process_number,"finished.")

def emeteur(process_number):
    if(process_number==1 or process_number==2 or process_number==3 or process_number== 4 or process_number==5):
        emeteur = True;
    else:
        emeteur = False;
    return emeteur

def recepteur(process_number):
    if(process_number==4 or process_number==5 or process_number==6 or process_number==7 or process_number==8):
        recepteur = True;
    else:
        recepteur = False;
    return recepteur

# Run following code when the program starts
if __name__ == '__main__':
   # Declare objects of MyThread class
   #var1 = int(input("Votre valeur a multiplier dans thread 1\n"))
   #myThreadOb1 = MyThread(4,1)
   #myThreadOb1.setName('Thread 1')
 
   #var2 = int(input("Votre valeur a multiplier dans thread 2\n"))
   #myThreadOb2 = MyThread(4,1.5)
   #myThreadOb2.setName('Thread 2')

   #var3 = int(input("Votre valeur a multiplier dans thread 3\n"))
   #myThreadOb3 = MyThread(4,0.2)
   #myThreadOb3.setName('Thread 3')

   #var4 = int(input("Votre valeur a multiplier dans thread 4\n"))
   #myThreadOb4 = MyThread(4,2.5)
   #myThreadOb4.setName('Thread 4')
 
   # Start running the threads!
   #myThreadOb1.start()
   #myThreadOb2.start()
   #myThreadOb3.start()
   #myThreadOb4.start()
 
   # Wait for the threads to finish...
   #myThreadOb1.join()
   #myThreadOb2.join()
   #myThreadOb3.join()
   #myThreadOb4.join()

   #Question 2 Partie 2 mais la y a 3 processus creer par contre
   mon_fichier = fichier_manipulation("resultat.txt");
   mon_fichier1 = fichier_manipulation("resultat1.txt");

   #Question 3 Partie 2
   #mon_fichier.lecture_affichage_fichier();
   p1 = Myprocess(1,5,0.1,2,mon_fichier)
   p2 = Myprocess(2,5,0.1,5,mon_fichier1)
   p3 = Myprocess(3,5,0.1,5,mon_fichier)
   p4 = Myprocess(4,5,0.1,5,mon_fichier)
   p5 = Myprocess(5,5,0.1,5,mon_fichier)
   p6 = Myprocess(6,5,0.1,5,mon_fichier)
   p7 = Myprocess(7,5,0.1,5,mon_fichier)
   p8 = Myprocess(8,5,0.1,5,mon_fichier)

   p1.start()
   p2.start()
   p4.start()

   p1.join()
   p2.join()
   p4.join()

   #mon_fichier.lecture_affichage_fichier();
   #mon_fichier1.lecture_affichage_fichier();

 
   print('Main Terminating...')

   #VOIR LES RESULTATS
   #myThreadOb1.print_result()
   #myThreadOb2.print_result()
   #myThreadOb3.print_result()
   #myThreadOb4.print_result()
#-----------------------------------#
# Laboratorio di sistemi operativi  #
# Classi - Round Robin              #
#-----------------------------------#

import random

class Processo:
    def __init__(self,Pid,MinSeqCPU,MaxSeqCPU,MinSeqIO,MaxSeqIO):
#inizializzo il pid del processo
		self.pid=str(Pid).zfill(5)
#inizializzo la durata minima della sequenza di CPU
		self.MinSeqCPU=MinSeqCPU
#inizializzo la durata massima della sequenza di CPU
		self.MaxSeqCPU=MaxSeqCPU
#inizializzo la durata minima della sequenza di I/O
		self.MinSeqIO=MinSeqIO
#inizializzo la durata massima della sequenza di I/O
		self.MaxSeqIO=MaxSeqIO
#lista contenente le sequenze di operazione un processo
		self.ListaSequenze=[]
		self.generaSequenza()

    def generaDurataSequenzaCpu(self):
		return random.randint(self.MinSeqCPU,self.MaxSeqCPU)

    def generaDurataSequenzaIO(self):
		return random.randint(self.MinSeqIO,self.MaxSeqIO)

    def generaSequenza(self):
                numSequenze=random.randint(1,2)
		for i in range(0,numSequenze):
			self.ListaSequenze.append(self.generaDurataSequenzaCpu())
			self.ListaSequenze.append(self.generaDurataSequenzaIO())
		#il processo deve finire con una sequenza di CPU
		self.ListaSequenze.append(self.generaDurataSequenzaCpu())

#Metodo che ritorna la serie di operazione di un singolo processo
    def getSequenza(self):
		return self.ListaSequenze
#Metodo che ritorna il pid di un processo
    def getPID(self):
		return self.pid
#Restituisce la durata della sequenza di CPU o I/O che si trova in testa alla lista.
    def getDurata(self):
            return self.ListaSequenze[0]
#Rimuove la durata della sequenza di CPU o I/O che si trova in testa alla lista.
    def popDurata(self):
		self.ListaSequenze.pop(0)

class Coda:
	def __init__(self):
		self.elementiCoda=[]
#aggiunge un singolo elemento
	def aggiungiProcesso(self,elemento):
		self.elementiCoda.append(elemento)
#aggiunge una lista di elementi
	def aggiungiLista(self,lista):
		self.elementiCoda.extend(lista)
#ritorna il numero di elementi della coda
	def getLunghezza(self):
		return len(self.elementiCoda)
#rimuove l'elemento in testa alla coda
	def rimuovi(self):
		return self.elementiCoda.pop(0)
#stampa i PID dei processi
	def stampainfo(self):
		for x in range(self.getLunghezza()):
                    	pid=self.elementiCoda[x].getPID()
                        print 'Processo '+str(pid)+' = '+ str(self.elementiCoda[x].getSequenza())
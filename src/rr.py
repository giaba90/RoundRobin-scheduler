#-----------------------------------#
# Laboratorio di sistemi operativi  #
# Scheduler Round Robin             #
#-----------------------------------#

import color_markup_string as cms

class RR:
    def __init__(self):
        self.flussoCpu='Inattiva'
        self.flussoIO='Inattiva'
        self.durataCpu=0
        self.durataIO=0
#Effettua la selezione di un processo da una coda.
    def dispatched(self, coda):
        #Rimuove l'elemento selezionato dalla coda.
        elementoSelezionato = coda.rimuovi()
        #Restituisce l'elemento selezionato (oggetto Processo), il PID, la sequenza di esecuzione.
        return elementoSelezionato, elementoSelezionato.getPID(),elementoSelezionato.getDurata()
#Determina se un processo ha terminato la sua esecuzione totale.
    def isMorto(self, listaSequenza):
        if len(listaSequenza):
            #Se la lista delle sequenze alternate di CPU e I/O non e' vuota il processo deve terminare la sua esecuzione totale.
            return False
        else:
            #Se la lista delle sequenze alternate di CPU e I/O e' vuota il processo ha terminato la sua esecuzione totale.
            return True
#Rilasciata la CPU, il processo viene aggiunto alla coda di I/O se deve eseguire operazioni di questa tipologia.
    def cambioContesto(self, processo, coda):
        #Elimina la sequenza del processo appena eseguita.
        processo.popDurata()
        #Se il processo non ha completato la sua esecuzione totale,
        if not self.isMorto(processo.getSequenza()):
            #viene aggiungo alla coda.
            coda.aggiungiProcesso(processo)

    def stampa(self,istante,flussoCPu,durataCpu,flussoIO,durataIO,codaCPU,codaIO):
            print cms.color("<yellow>istante: </yellow>")+str(istante)+"s"
            print "Processo in eseguzione: "+self.flussoCpu+" con durata: "+str(self.durataCpu)+ 's'
            if codaCPU.getLunghezza()==0:
                print "La coda dei processi pronti e' vuota"
            else:
                print "La coda dei processi pronti e' popolata da: "
                codaCPU.stampainfo()
            print "Processo in IO: "+self.flussoIO+" con durata:"+str(self.durataIO)+'s'
            if codaIO.getLunghezza()==0:
                print "La coda di I/O e' vuota"
            else:
                print "Coda IO: "
                codaIO.stampainfo()

    def scheduler(self,quanto,codaCPU,codaIO):
        flag=''#se il proc. ha finito la sua seq. di CPU vale 0 altrimenti il flag vale 1 se deve tornare in ready queue
        istante=0
        finito=bool(0) #e' falso
        while (not finito): #finche' e' vero
#------------------------------------gestione della Cpu--------------------------------------#
#coda piena e cpu vuota
            if(codaCPU.getLunghezza()!=0)and(self.flussoCpu=="Inattiva"):
                elementoDispatchedCPU, pidDispatchedCPU, durataDispatchedCPU = self.dispatched(codaCPU)
#primo caso la durata e' maggiore del quanto
                if durataDispatchedCPU > quanto:
                    resto=durataDispatchedCPU-quanto
                    elementoDispatchedCPU.ListaSequenze[0]=resto
                    self.durataCpu=quanto
                    self.flussoCpu=pidDispatchedCPU
                    print cms.color("<red>PROCESSO SCELTO PER L'ESECUZIONE:</red>")+str(pidDispatchedCPU)
                    flag=1
#secondo e terzo caso la durata e' minore o uguale al quanto
                elif durataDispatchedCPU <= quanto:
                    self.durataCpu=durataDispatchedCPU
                    self.flussoCpu=pidDispatchedCPU
                    print cms.color("<red>PROCESSO SCELTO PER L'ESECUZIONE:</red>")+str(pidDispatchedCPU)
                    flag=0 
#coda piena ed cpu piena
            elif ((codaCPU.getLunghezza() != 0)and(self.flussoCpu!="Inattiva")):
                if(self.durataCpu==0): #ma il processo ha finito il quanto
                    if flag==1:
                        codaCPU.aggiungiProcesso(elementoDispatchedCPU)
                    elif flag==0:
                        self.cambioContesto(elementoDispatchedCPU, codaIO)
#prendo il primo processo
                    elementoDispatchedCPU, pidDispatchedCPU, durataDispatchedCPU = self.dispatched(codaCPU)
#primo caso la durata e' maggiore del quanto
                    if durataDispatchedCPU > quanto:
                        resto=durataDispatchedCPU-quanto
                        elementoDispatchedCPU.ListaSequenze[0]=resto
                        self.durataCpu=quanto
                        self.flussoCpu=pidDispatchedCPU
                        print cms.color("<red>PROCESSO SCELTO PER L'ESECUZIONE:</red>")+str(pidDispatchedCPU)
                        flag=1
#secondo e terzo caso la durata e' minore o uguale al quanto
                    elif durataDispatchedCPU <= quanto:
                        self.durataCpu=durataDispatchedCPU
                        self.flussoCpu=pidDispatchedCPU
                        print cms.color("<red>PROCESSO SCELTO PER L'ESECUZIONE:</red>")+str(pidDispatchedCPU)
                        flag=0      
#coda vuota e la cpu e' piena    
            elif(codaCPU.getLunghezza()==0)and(self.flussoCpu!="Inattiva"):
                if(self.durataCpu==0): #ma il processo ha finito il quanto
                    if flag==1: #viene mandato in coda
                        codaCPU.aggiungiProcesso(elementoDispatchedCPU)
                        #ma viene riscelto in quanto unico processo in coda
                        elementoDispatchedCPU, pidDispatchedCPU, durataDispatchedCPU = self.dispatched(codaCPU)
                        #primo caso la durata e' maggiore del quanto
                        if durataDispatchedCPU > quanto:
                            resto=durataDispatchedCPU-quanto
                            elementoDispatchedCPU.ListaSequenze[0]=resto
                            self.durataCpu=quanto
                            self.flussoCpu=pidDispatchedCPU
                            print cms.color("<red>PROCESSO SCELTO PER L'ESECUZIONE:</red>")+str(pidDispatchedCPU)
                            flag=1
#secondo e terzo caso la durata e' minore o uguale al quanto
                        elif durataDispatchedCPU <= quanto:
                            self.durataCpu=durataDispatchedCPU
                            self.flussoCpu=pidDispatchedCPU
                            print cms.color("<red>PROCESSO SCELTO PER L'ESECUZIONE:</red>")+str(pidDispatchedCPU)
                            flag=0
                #se ha finito il quanto e non ha piu' istruzioni,setto la cpu inattiva
                    elif flag==0:
                        self.cambioContesto(elementoDispatchedCPU, codaIO)
                        self.flussoCpu="Inattiva"
#------------------------------------gestione dell' I/O-----------------------------------#
       #coda piena ed i/o piena ma processo morto
            if(codaIO.getLunghezza()!=0)and(self.flussoIO!="Inattiva"):
                if(self.durataIO==0):
                    self.cambioContesto(elementoDispatchedIO, codaCPU)
                    elementoDispatchedIO, pidDispatchedIO, durataDispatchedIO = self.dispatched(codaIO)
                    self.durataIO=durataDispatchedIO
                    self.flussoIO=pidDispatchedIO
       #coda piena e la i/o e' vuota
            elif (codaIO.getLunghezza()!=0)and(self.flussoIO=="Inattiva"): 
                elementoDispatchedIO, pidDispatchedIO, durataDispatchedIO = self.dispatched(codaIO)
                self.durataIO=durataDispatchedIO
                self.flussoIO=pidDispatchedIO
       #coda vuota e la i/o e' piena ma il processo ha finito
            elif(codaIO.getLunghezza()==0)and(self.flussoIO!="Inattiva"):
                if(self.durataIO==0):
                    self.cambioContesto(elementoDispatchedIO, codaCPU)
                    self.flussoIO="Inattiva"
            #coda cpu/io vuota e cpu/io vuota
            if (codaCPU.getLunghezza() == 0)and(self.durataCpu==0):
                if (codaIO.getLunghezza() == 0)and(self.durataIO==0):
                    finito=not finito
#-----------------------------------stampa dei processi-----------------------------------#
            self.stampa(istante,self.flussoCpu,self.flussoIO,self.durataCpu,self.durataIO,codaCPU,codaIO)
#----------------------------------gestione della timeline--------------------------------#
            if(self.durataCpu!=0):
		self.durataCpu=self.durataCpu-1
            if(self.durataIO!=0):
		self.durataIO=self.durataIO-1
            istante=istante+1
#-----------------------------------#
# Laboratorio di sistemi operativi  #
# Scheduler Round Robin - Main      #
#-----------------------------------#

from struct import Coda
from struct import Processo
from rr import *
import sys

import color_markup_string as cms

help = '''************************************
* Laboratorio di Sistemi operativi *
* Progetto: Scheduler Round Robin  *
************************************

Indicare da linea di comando:

- numero dei processi da considerare durante la simulazione
- durata minina della sequenza di Cpu
- duarata massima della sequenza di Cpu
- durata minima della sequenza di I/O
- durata massima della sequenza di I/O
- quanto di tempo

Esempio: python main.py 4 1 4 1 3 2
        '''

if (len(sys.argv)<=1):
	print help
else:
    numProcessiSimulazione = int(sys.argv[1])
    durataMinSeqCPU=int(sys.argv[2])
    durataMaxSeqCPU=int(sys.argv[3])
    durataMinSeqIO=int(sys.argv[4])
    durataMaxSeqIO=int(sys.argv[5])
    quanto=int(sys.argv[6])
    try:

#dichiaro le strutture necessarie allo scheduler
        codaProcessiPronti=Coda()
        codaIO=Coda()
        print cms.color("<green>#--- I processi creati sono ---#\n</green>")
# creazione lista dei processi
        p=[Processo(Pid,durataMinSeqCPU,durataMaxSeqCPU,durataMinSeqIO,durataMaxSeqIO)for Pid in range (numProcessiSimulazione)]
#aggiungi i processi alla coda
        codaProcessiPronti.aggiungiLista(p)
#stampo la coda dei processi pronti
        codaProcessiPronti.stampainfo()
        print cms.color("<green>\nIl quanto di tempo e': </green>")+str(quanto)+"s"
        print cms.color("<green>#-------------------------------#</green>")
   #avvio lo scheduler
        print cms.color("<blue>\nINIZIO SIMULAZIONE\n</blue>")
        algoritmo=RR()
        algoritmo.scheduler(quanto, codaProcessiPronti, codaIO)
        print cms.color("<blue>\nFINE SIMULAZIONE\n</blue>")

    except KeyboardInterrupt:
	print ""
	print "[*] Exiting..."
	print ""
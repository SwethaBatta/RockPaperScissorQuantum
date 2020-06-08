# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 08:13:00 2020

@author: SwethaBatta
"""

import qiskit as qk
from qiskit import IBMQ

#Add your Qiskit API token below
#IBMQ.save_account('')

# Load saved account from memory
IBMQ.load_account()

n = 3
q = qk.QuantumRegister(n)
c = qk.ClassicalRegister(n)
circ = qk.QuantumCircuit(q, c)

for j in range(n):
    circ.h(q[j])
    
circ.measure(q,c)

print (circ)

backend = qk.BasicAer.get_backend('qasm_simulator')

def rand_int():
    new_job = qk.execute(circ, backend, shots=1)
    bitstring = new_job.result().get_counts()
    bitstring = list(bitstring.keys())[0]
    integer = int(bitstring, 2)
    return integer

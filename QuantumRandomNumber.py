# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 08:13:00 2020

@author: SwethaBatta
"""

import qiskit as qk
from qiskit import IBMQ

#Add your Qiskit API token below
#IBMQ.save_account('0bab1b8ae71f47561a135706a33012b3c8d37077df31f351f8ac365c43e2ae7572de93ea4b960d6cbc68572219a42e17e154194364afd2a12f44d88b1bafbb04')

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

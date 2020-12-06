#!/usr/bin/env python
# coding: utf-8

# In[2]:


from qiskit import *
get_ipython().run_line_magic('matplotlib', 'inline')
from qiskit.tools.visualization import plot_histogram


# In[3]:


secretnumber = '101001'


# In[16]:


circuit = QuantumCircuit(6+1, 6)

circuit.h([0,1,2,3,4,5])
circuit.x(6)
circuit.h(6)

circuit.barrier()

circuit.cx(5, 6)
circuit.cx(3, 6)
circuit.cx(0, 6)

circuit.barrier()
circuit.h([0,1,2,3,4,5])
circuit.barrier()
circuit.measure([0,1,2,3,4,5], [0,1,2,3,4,5])


# In[17]:


circuit.draw(output='mpl')


# In[19]:


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator, shots=1).result()
counts = result.get_counts()
print(counts)


# In[32]:


circuit_n = QuantumCircuit(len(secretnumber)+1, len(secretnumber))

circuit_n.h(range(len(secretnumber)))
circuit_n.x(len(secretnumber))
circuit_n.h(len(secretnumber))

circuit_n.barrier()

for ii, yesno in enumerate(reversed(secretnumber)):
    if yesno == '1':
        circuit_n.cx(ii, len(secretnumber))

circuit_n.barrier()
circuit_n.h(range(len(secretnumber)))
circuit_n.barrier()
circuit_n.measure(range(len(secretnumber)), range(len(secretnumber)))


# In[33]:


circuit.draw(output='mpl')


# In[31]:


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator, shots=1).result()
counts = result.get_counts()
print(counts)


# In[ ]:





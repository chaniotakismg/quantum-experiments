#!/usr/bin/env python
# coding: utf-8

# In[2]:


from qiskit import *


# In[3]:


circuit = QuantumCircuit(3, 3)


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
circuit.draw(output='mpl')


# In[5]:


circuit.x(0)
circuit.barrier()
circuit.draw(output='mpl')


# In[6]:


circuit.h(1)
circuit.cx(1,2)


# In[7]:


circuit.draw(output='mpl')


# In[8]:


circuit.cx(0,1)
circuit.h(0)
circuit.draw(output='mpl')


# In[9]:


circuit.barrier()
circuit.measure([0,1], [0,1])
circuit.draw(output='mpl')


# In[10]:


# Quantum Teleportation protocol
circuit.barrier()
circuit.cx(1,2)
circuit.cz(0,2)
circuit.draw(output='mpl')


# In[13]:


circuit.measure(2,2)
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator, shots=1024).result()
counts = result.get_counts()
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)


# In[14]:


print(counts)


# In[ ]:





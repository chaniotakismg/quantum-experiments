from qiskit import *
from qiskit.tools import job_monitor
from qiskit.tools.visualization import plot_histogram

if __name__ == '__main__':

    circuit = QuantumCircuit(3, 3)
    circuit.x(0)
    circuit.barrier()
    circuit.h(1)
    circuit.cx(1,2)
    circuit.cx(0,1)
    circuit.h(0)
    circuit.barrier()

    # Quantum "Teleportation"
    circuit.barrier()
    circuit.cx(1,2)
    circuit.cz(0,2)
    circuit.measure(2, 2)

    IBMQ.load_account()
    provider = IBMQ.get_provider(hub='ibm-q')
    device = provider.get_backend('ibmq_santiago')
    job = execute(circuit, backend=device, shots=1024)
    print("Job ID:", job.job_id())
    job_monitor(job)
    result = job.result()
    counts = result.get_counts()

    plot_histogram(counts)
    print(counts)

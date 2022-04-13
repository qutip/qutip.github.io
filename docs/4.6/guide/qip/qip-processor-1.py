from qutip import basis
from qutip.qip.circuit import QubitCircuit
from qutip.qip.device import LinearSpinChain

qc = QubitCircuit(2)
qc.add_gate("X", targets=0)
qc.add_gate("X", targets=1)
processor = LinearSpinChain(2)
processor.load_circuit(qc)
fig, axis = processor.plot_pulses()
fig.show()
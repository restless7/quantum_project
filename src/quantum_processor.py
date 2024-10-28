import torch
import math
from typing import Dict, Optional, Tuple
from complextensor import ComplexTensor

class QuantumProcessor:
    """
    Processes quantum states and applies quantum transformations
    """
    def __init__(self):
        self.state: Optional[ComplexTensor] = None
        self.history: list = []

    def create_state(self, data: Dict) -> ComplexTensor:
        """
        Create a quantum state from data
        
        Args:
            data (Dict): Dictionary containing 'real' and 'imaginary' parts
        
        Returns:
            ComplexTensor: The quantum state
        """
        real = torch.tensor(data['wavefunction']['real'], dtype=torch.float32)
        imag = torch.tensor(data['wavefunction']['imaginary'], dtype=torch.float32)
        
        self.state = ComplexTensor(real, imag)
        self.history.append(('create', self.state.abs() ** 2))
        return self.state

    def apply_hadamard(self) -> ComplexTensor:
        """Apply Hadamard transformation"""
        if self.state is None:
            raise ValueError("No quantum state initialized")
            
        h_factor = 1/math.sqrt(2)
        hadamard = ComplexTensor(
            torch.tensor([[h_factor, h_factor], 
                         [h_factor, -h_factor]], dtype=torch.float32),
            torch.zeros((2, 2), dtype=torch.float32)
        )
        
        self.state = self._apply_gate(hadamard, self.state)
        self.history.append(('hadamard', self.state.abs() ** 2))
        return self.state

    def apply_pauli_x(self) -> ComplexTensor:
        """Apply Pauli-X (NOT) gate"""
        if self.state is None:
            raise ValueError("No quantum state initialized")
            
        pauli_x = ComplexTensor(
            torch.tensor([[0., 1.], 
                         [1., 0.]], dtype=torch.float32),
            torch.zeros((2, 2), dtype=torch.float32)
        )
        
        self.state = self._apply_gate(pauli_x, self.state)
        self.history.append(('pauli_x', self.state.abs() ** 2))
        return self.state

    def apply_pauli_z(self) -> ComplexTensor:
        """Apply Pauli-Z (phase) gate"""
        if self.state is None:
            raise ValueError("No quantum state initialized")
            
        pauli_z = ComplexTensor(
            torch.tensor([[1., 0.], 
                         [0., -1.]], dtype=torch.float32),
            torch.zeros((2, 2), dtype=torch.float32)
        )
        
        self.state = self._apply_gate(pauli_z, self.state)
        self.history.append(('pauli_z', self.state.abs() ** 2))
        return self.state

    def _apply_gate(self, gate: ComplexTensor, state: ComplexTensor) -> ComplexTensor:
        """Apply a quantum gate to a state"""
        g_real, g_imag = gate.real, gate.imag
        s_real = state.real.unsqueeze(1)
        s_imag = state.imag.unsqueeze(1)
        
        result_real = torch.mm(g_real, s_real) - torch.mm(g_imag, s_imag)
        result_imag = torch.mm(g_real, s_imag) + torch.mm(g_imag, s_real)
        
        return ComplexTensor(result_real.squeeze(), result_imag.squeeze())

    def get_probabilities(self) -> torch.Tensor:
        """Get measurement probabilities of current state"""
        if self.state is None:
            raise ValueError("No quantum state initialized")
        return self.state.abs() ** 2

    def get_state_history(self) -> list:
        """Get history of transformations and their results"""
        return self.history
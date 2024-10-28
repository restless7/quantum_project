import json
import numpy as np
from typing import Dict, Any, Optional
import torch
from complextensor import ComplexTensor

class DataHandler:
    """Handles quantum data loading and validation"""
    
    def __init__(self):
        self.data: Optional[Dict] = None
    
    def load_data(self, file_path: str) -> Dict[str, Any]:
        """
        Load quantum data from JSON file
        """
        try:
            with open(file_path, 'r') as f:
                self.data = json.load(f)
            self._validate_data()
            return self.data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")
    
    def _validate_data(self) -> None:
        """
        Validate data structure and contents
        """
        if not self.data:
            raise ValueError("No data loaded")
        
        required_fields = ['wavefunction']
        if not all(field in self.data for field in required_fields):
            raise ValueError(f"Missing required fields: {required_fields}")
        
        wf = self.data['wavefunction']
        if not all(k in wf for k in ['real', 'imaginary']):
            raise ValueError("Wavefunction must have real and imaginary parts")
        
        if len(wf['real']) != len(wf['imaginary']):
            raise ValueError("Real and imaginary parts must have same length")
    
    def get_quantum_state(self) -> ComplexTensor:
        """
        Convert loaded data to ComplexTensor
        """
        if not self.data:
            raise ValueError("No data loaded")
        
        real_part = torch.tensor(self.data['wavefunction']['real'], dtype=torch.float32)
        imag_part = torch.tensor(self.data['wavefunction']['imaginary'], dtype=torch.float32)
        
        return ComplexTensor(real_part, imag_part)
    
    def save_data(self, data: Dict[str, Any], file_path: str) -> None:
        """
        Save quantum data to JSON file
        """
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
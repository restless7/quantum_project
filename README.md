# Quantum Data Analysis Tool

A Python toolkit for quantum state analysis and transformation using ComplexTensor.

## Features

- Quantum state data reading and validation
- Complex quantum transformations
- Visualization of quantum states
- Comprehensive unit testing suite
- Support for multiple quantum gates (Hadamard, Pauli-X, Pauli-Z)

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from src.quantum_processor import QuantumProcessor
from src.data_handler import DataHandler

# Load and process quantum data
data_handler = DataHandler()
quantum_data = data_handler.load_data("data/sample_quantum_states.json")

# Create quantum processor
processor = QuantumProcessor()
state = processor.create_state(quantum_data)

# Apply transformations
transformed_state = processor.apply_hadamard(state)
```

## Testing

Run the test suite:

```bash
python -m pytest tests/
```

## Project Structure

- `src/`: Source code
- `tests/`: Unit tests
- `examples/`: Usage examples
- `data/`: Sample data files

## Requirements

- Python 3.8+
- ComplexTensor
- PyTorch
- NumPy
- Matplotlib

# quantum_project
Quantum state analysis and transformation toolkit using ComplexTensor

A Python toolkit for quantum state analysis and transformation using ComplexTensor.

## Features
- Quantum state data reading and validation
- Complex quantum transformations (Hadamard, Pauli-X, Pauli-Z)
- Visualization of quantum states
- Comprehensive unit testing suite

## Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\Activate
# Linux/Mac:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
pip install -e .
```

## Usage

Basic example:
```python
from src.quantum_processor import QuantumProcessor
from src.visualization import QuantumVisualizer

# Initialize components
processor = QuantumProcessor()
visualizer = QuantumVisualizer()

# Create quantum state
data = {
    "wavefunction": {
        "real": [1.0, 0.0],
        "imaginary": [0.0, 0.0]
    }
}

# Apply transformations
state = processor.create_state(data)
processor.apply_hadamard()
processor.apply_pauli_x()

# Visualize results
visualizer.plot_transformation_sequence(processor.get_state_history())
```

## Project Structure
```
quantum_project/
├── src/               # Source code
├── tests/             # Unit tests
├── examples/          # Usage examples
└── data/             # Sample data files
```

## Running Tests
```bash
python -m pytest tests/
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

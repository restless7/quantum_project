import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_handler import DataHandler
from src.quantum_processor import QuantumProcessor
from src.visualization import QuantumVisualizer

def main():
    # Initialize components
    data_handler = DataHandler()
    processor = QuantumProcessor()
    visualizer = QuantumVisualizer()
    
    try:
        # Load quantum data
        data = {
            "wavefunction": {
                "real": [1.0, 0.0],
                "imaginary": [0.0, 0.0]
            }
        }
        
        # Create quantum state
        state = processor.create_state(data)
        print("\nInitial state created")
        visualizer.plot_state(processor.get_probabilities(), "Initial State")
        
        # Apply transformations
        processor.apply_hadamard()
        print("\nApplied Hadamard transformation")
        visualizer.plot_state(processor.get_probabilities(), "After Hadamard")
        
        processor.apply_pauli_x()
        print("\nApplied Pauli-X transformation")
        visualizer.plot_state(processor.get_probabilities(), "After Pauli-X")
        
        # Show transformation sequence
        print("\nPlotting transformation sequence")
        visualizer.plot_transformation_sequence(processor.get_state_history())
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
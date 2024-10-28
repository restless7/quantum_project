import matplotlib.pyplot as plt
import torch
from typing import List, Tuple, Optional
import numpy as np

class QuantumVisualizer:
    """
    Visualizes quantum states and transformations
    """
    def __init__(self):
        self.figure_size = (10, 6)
        self.colors = ['#2196F3', '#4CAF50', '#F44336']  # Material design colors
        
    def plot_state(self, probabilities: torch.Tensor, title: str) -> None:
        """
        Plot quantum state probabilities
        
        Args:
            probabilities: Tensor of probabilities
            title: Plot title
        """
        plt.figure(figsize=self.figure_size)
        probs_numpy = probabilities.detach().numpy()
        
        plt.bar(['|0⟩', '|1⟩'], probs_numpy, color=self.colors[0])
        plt.ylim(0, 1)
        plt.title(title)
        plt.ylabel('Probability')
        
        # Add probability values on top of bars
        for i, prob in enumerate(probs_numpy):
            plt.text(i, prob + 0.05, f'{prob:.3f}', ha='center')
            
        plt.show()

    def plot_transformation_sequence(self, 
                                  history: List[Tuple[str, torch.Tensor]], 
                                  save_path: Optional[str] = None) -> None:
        """
        Plot sequence of transformations
        
        Args:
            history: List of (transformation_name, probabilities) tuples
            save_path: Optional path to save the plot
        """
        n_transforms = len(history)
        plt.figure(figsize=(12, 4 * n_transforms))
        
        for idx, (transform, probs) in enumerate(history):
            plt.subplot(n_transforms, 1, idx + 1)
            probs_numpy = probs.detach().numpy()
            
            plt.bar(['|0⟩', '|1⟩'], probs_numpy, color=self.colors[idx % len(self.colors)])
            plt.ylim(0, 1)
            plt.title(f"After {transform.replace('_', ' ').title()}")
            plt.ylabel('Probability')
            
            for i, prob in enumerate(probs_numpy):
                plt.text(i, prob + 0.05, f'{prob:.3f}', ha='center')
        
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def plot_bloch_sphere(self, state_vector: torch.Tensor) -> None:
        """
        Plot quantum state on Bloch sphere (simplified 2D projection)
        
        Args:
            state_vector: Complex quantum state vector
        """
        fig = plt.figure(figsize=self.figure_size)
        ax = fig.add_subplot(111, projection='polar')
        
        # Convert state vector to angles
        theta = torch.angle(state_vector[0])
        phi = torch.angle(state_vector[1])
        
        # Plot on polar coordinates
        ax.plot([theta, phi], [1, 1], 'o-', label='State vector')
        ax.set_title('Bloch Sphere Projection')
        plt.show()
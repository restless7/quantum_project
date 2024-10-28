import unittest
import os
import json
import torch
from src.data_handler import DataHandler

class TestDataHandler(unittest.TestCase):
    def setUp(self):
        self.data_handler = DataHandler()
        self.test_data = {
            "wavefunction": {
                "real": [1.0, 0.0],
                "imaginary": [0.0, 0.0]
            }
        }
        
        # Create test data file
        with open('test_data.json', 'w') as f:
            json.dump(self.test_data, f)
    
    def tearDown(self):
        # Clean up test file
        if os.path.exists('test_data.json'):
            os.remove('test_data.json')
    
    def test_load_data(self):
        """Test data loading functionality"""
        data = self.data_handler.load_data('test_data.json')
        self.assertEqual(data, self.test_data)
    
    def test_invalid_file(self):
        """Test handling of non-existent file"""
        with self.assertRaises(FileNotFoundError):
            self.data_handler.load_data('nonexistent.json')
    
    def test_invalid_data_structure(self):
        """Test handling of invalid data structure"""
        invalid_data = {"invalid": "data"}
        with open('test_data.json', 'w') as f:
            json.dump(invalid_data, f)
        
        with self.assertRaises(ValueError):
            self.data_handler.load_data('test_data.json')
    
    def test_get_quantum_state(self):
        """Test quantum state creation"""
        self.data_handler.load_data('test_data.json')
        state = self.data_handler.get_quantum_state()
        
        self.assertTrue(torch.allclose(state.real, torch.tensor([1.0, 0.0])))
        self.assertTrue(torch.allclose(state.imag, torch.tensor([0.0, 0.0])))

if __name__ == '__main__':
    unittest.main()
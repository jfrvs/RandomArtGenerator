import math
import numpy as np

def random_walk(number_of_steps, possible_directions):
    angles = np.linspace(0, 2 * np.pi, possible_directions, endpoint=False, dtype=np.float32)
    
    chosen_angles = np.random.choice(angles, size=number_of_steps).astype(np.float32)
    
    steps = np.column_stack((np.sin(chosen_angles), np.cos(chosen_angles))).astype(np.float32)
    
    return np.vstack(([0, 0], np.cumsum(steps, axis=0, dtype=np.float32)))
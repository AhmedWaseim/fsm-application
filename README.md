# Traffic Light Finite State Machine

A simple implementation of a traffic light system using Finite State Machine (FSM) principles.

## Features
- Three states: RED, GREEN, YELLOW
- Deterministic state transitions
- Simulation capabilities
- Unit tests

## States and Transitions
- RED → GREEN
- GREEN → YELLOW  
- YELLOW → RED

## Usage
```python
from src.traffic_light import TrafficLight

# Create traffic light instance
tl = TrafficLight()

# Change states
tl.change()  # RED -> GREEN
tl.change()  # GREEN -> YELLOW
tl.change()  # YELLOW -> RED

# Simulate cycles
tl.simulate_cycle(2)  # Simulate 2 complete cycles
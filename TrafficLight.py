class TrafficLight:
    def __init__(self):
        self.state = "RED"
        self.transitions = {
            "RED": "GREEN",
            "GREEN": "YELLOW", 
            "YELLOW": "RED"
        }
    
    def change(self):
        """Move to next state"""
        self.state = self.transitions[self.state]
        return self.state
    
    def get_state(self):
        """Get current state"""
        return self.state
    
    def simulate_cycle(self, cycles=1):
        """Simulate complete traffic light cycles"""
        for i in range(cycles * 3):  # 3 states per cycle
            print(f"Current state: {self.state}")
            self.change()
        print(f"Final state: {self.state}")

# Example usage
if __name__ == "__main__":
    tl = TrafficLight()
    print("Initial state:", tl.get_state())
    
    # Simulate one complete cycle
    print("\nSimulating one cycle:")
    tl.simulate_cycle(1)

import random
import time

class Threat:
    def __init__(self, id, distance):
        self.id = id
        self.distance = distance  # Distance from the defense system

class IronDome:
    def __init__(self):
        self.interceptions = 0
        self.threats = []

    def detect_threat(self, threat):
        print(f"Threat detected! ID: {threat.id}, Distance: {threat.distance} km")
        self.threats.append(threat)

    def assess_threat(self, threat):
        # Assume a threat is considered for interception if it's within 10 km
        if threat.distance < 10:
            return True
        return False

    def intercept_threat(self, threat):
        if self.assess_threat(threat):
            print(f"Interception launched for Threat ID: {threat.id}")
            time.sleep(1)  # Simulating interception time
            print(f"Threat ID: {threat.id} intercepted successfully!")
            self.interceptions += 1
        else:
            print(f"Threat ID: {threat.id} is not a threat. Ignoring.")

    def run_simulation(self):
        for i in range(1, 6):  # Simulate 5 threats
            distance = random.randint(1, 20)  # Random distance from 1 to 20 km
            threat = Threat(i, distance)
            self.detect_threat(threat)
            self.intercept_threat(threat)

        print(f"\nTotal interceptions: {self.interceptions}")

if __name__ == "__main__":
    dome = IronDome()
    dome.run_simulation()

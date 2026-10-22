import random
import time
from datetime import datetime

 
NUM_RACKS = 5
SERVERS_PER_RACK = 20

def generate_server_data(rack_id, server_id):
    # Normal workload
    cpu = random.uniform(5, 95)
    gpu = random.uniform(0, 90)

    # Occasionally create an idle/zombie server
    zombie = random.random() < 0.05

    if zombie:
        cpu = random.uniform(0, 4)
        gpu = 0
        workload = 0
        power = random.uniform(220, 320)
        temperature = random.uniform(28, 38)
        status = "ZOMBIE_CANDIDATE"

    else:
        workload = (cpu + gpu) / 2

        # Simplified power model
        power = 180 + (cpu * 2.2) + (gpu * 1.5)

        # Simplified temperature model
        temperature = 25 + (power / 25) + random.uniform(-2, 2)

        status = "ACTIVE"

    humidity = random.uniform(35, 60)

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "rack_id": rack_id,
        "server_id": server_id,
        "cpu_usage": round(cpu, 2),
        "gpu_usage": round(gpu, 2),
        "power_watts": round(power, 2),
        "temperature_c": round(temperature, 2),
        "humidity_percent": round(humidity, 2),
        "workload_percent": round(workload, 2),
        "status": status
    }


def simulate_data_center():
    print("=" * 75)
    print("        AI DATA CENTER ENERGY OPTIMIZER")
    print("              STEP 1: SIMULATOR")
    print("=" * 75)

    print(f"Racks: {NUM_RACKS}")
    print(f"Servers per rack: {SERVERS_PER_RACK}")
    print(f"Total servers: {NUM_RACKS * SERVERS_PER_RACK}")
    print("=" * 75)

    while True:

        total_power = 0
        thermal_alerts = 0
        zombie_servers = 0

        print("\n" + "-" * 75)
        print("NEW SENSOR READING")
        print("-" * 75)

        for rack in range(1, NUM_RACKS + 1):

            for server in range(1, SERVERS_PER_RACK + 1):

                server_id = f"R{rack:02d}-S{server:02d}"

                data = generate_server_data(
                    rack_id=rack,
                    server_id=server_id
                )

                total_power += data["power_watts"]

                if data["temperature_c"] > 80:
                    thermal_alerts += 1

                if data["status"] == "ZOMBIE_CANDIDATE":
                    zombie_servers += 1

                # Print only interesting events
                if (
                    data["status"] == "ZOMBIE_CANDIDATE"
                    or data["temperature_c"] > 80
                ):
                    print(
                        f"{data['timestamp']} | "
                        f"{data['server_id']} | "
                        f"CPU {data['cpu_usage']:5.1f}% | "
                        f"GPU {data['gpu_usage']:5.1f}% | "
                        f"Power {data['power_watts']:6.1f} W | "
                        f"Temp {data['temperature_c']:5.1f} C | "
                        f"{data['status']}"
                    )

        print("\nDATA CENTER SUMMARY")
        print(f"Total power:       {total_power / 1000:.2f} kW")
        print(f"Zombie candidates: {zombie_servers}")
        print(f"Thermal alerts:    {thermal_alerts}")
        print("-" * 75)

        # Wait before generating the next set of readings
        time.sleep(3)


if __name__ == "__main__":
    try:
        simulate_data_center()

    except KeyboardInterrupt:
        print("\n\nSimulation stopped.")
        print("AI Data Center Simulator terminated.")
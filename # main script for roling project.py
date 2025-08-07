# main script for roling project
import sys
import json
from pathlib import Path
import logging
import subprocess

## get user input
def get_user_input():
    machine = []

get_user_input = input("do you want to start a new machine? (yes/no): ").strip().lower()
if get_user_input not in ['yes', 'no']: 
    
    sys.exit(1) 
if get_user_input == 'yes':
    machine_name = input("Enter the name of the new machine: ").strip()
    if not machine_name:
        print("Machine name cannot be empty.")
        sys.exit(1)
    
   
    # Initialize a basic configuration file
    config = {
        "name": machine_name,
        "os": (enter_os := input("Enter the operating system (e.g., Linux, Windows): ").strip()),
        "cpu": (enter_cpu := input("enter the cpu usege (e.g., 2 cores): ").strip()),
        "ram": (enter_ram := input("enter the ram usege (e.g., 4GB): ").strip()),
        "class": (enter_class := input("enter the class of the machine (e.g., web server, database): ").strip()),
    }

    
    # Save the configuration to a JSON file
    config_file = Path(f"{machine_name}_config.json")
    with config_file.open('w') as f:
        json.dump(config, f, indent=4)
    
    print(f"Configuration for {machine_name} saved to {config_file}"   )
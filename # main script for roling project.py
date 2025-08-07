# main script for roling project
import sys
import json
from pathlib import Path
import logging
import subprocess

## get user input
get_user_input = input("do you want to start a new machine? (yes/no): ").strip().lower()
if get_user_input not in ['yes', 'no']: 
    print("Invalid input. Please enter 'yes' or 'no'.")
    sys.exit(1) 
if get_user_input == 'yes':
    machine_name = input("Enter the name of the new machine: ").strip()
    if not machine_name:
        print("Machine name cannot be empty.")
        sys.exit(1)
    
    # Create a new machine directory
    machine_dir = Path(f"./machines/{machine_name}")
    machine_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize a basic configuration file
    config = {
        "name": machine_name,
        "status": "new"
    }
    
    with open(machine_dir / 'config.json', 'w') as f:
        json.dump(config, f, indent=4)
    
    print(f"New machine '{machine_name}' created successfully.")    
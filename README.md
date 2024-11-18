# Project Setup

This guide provides the steps to set up the environment for the project using `mambaforge` and `boltz-1`.

## Installation

Follow these commands to set up the environment and install the boltz-1:

```bash
# Add mambaforge to your module path
module add mambaforge

# Create a new conda environment with Python 3.10
mamba create --prefix /storage/{CITY}/home/{USER}/boltz python=3.10 -y

# Activate the newly created environment
mamba activate /storage/{CITY}/home/{USER}/boltz

# Set PYTHONUSERBASE to your environment directory
export PYTHONUSERBASE=/storage/{CITY}/home/{USER}/boltz/

# Install boltz-1 using pip
pip install boltz --user
```

## Run Boltz-1

Follow these commands to run boltz-1 on metacentrum:

```bash
# Example of command to run interactive environment for boltz-1
qsub -I -l walltime=4:0:0 -q gpu@pbs-m1.metacentrum.cz -l select=1:ncpus=1:ngpus=1:mem=20gb:scratch_local=10gb

# Add mambaforge to your module path
module add mambaforge

# Activate the environment
mamba activate /storage/{CITY}/home/{USER}/boltz

# Set PYTHONPATH to ensure the right version of python and its packages are used
export PYTHONPATH=/storage/{CITY}/home/{USER}/boltz/lib/python3.10/site-packages/
```

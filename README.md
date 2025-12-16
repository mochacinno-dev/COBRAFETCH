# COBRAFETCH

A sleek system information fetcher that combines the power of Python and Ruby.

## Features

- **Kernel & OS Detection** - System and distribution information
- **Hardware Info** - CPU, GPU, RAM, and device model
- **Desktop Environment** - Current DE/WM detection
- **Shell & Uptime** - Active shell and system uptime
- **Package Count** - Installed packages across different package managers

## Installation

```bash
# Clone the repository
git clone https://github.com/mochacinno-dev/COBRAFETCH.git
cd cobrafetch

# Install Python dependencies
pip install py-cpuinfo psutil distro
```

## Usage

```bash
python3 main.py
```
or
```sh
python main.py
```

## Requirements

- Python 3.6+
- Ruby 2.0+

## Tech Stack

- **Python** - Core system detection and hardware info
- **Ruby** - Shell, uptime, and package management

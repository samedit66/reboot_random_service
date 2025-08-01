# Random Interval Reboot Service

This Windows Service reboots the computer at random intervals between 10 and 60 minutes.

## Prerequisites
- Python 3.x installed
- Administrative privileges
- `pywin32` Python package

## Installation

1. **Install pywin32**  
   ```powershell
   pip install pywin32
   ```
2. **Copy the script**  
   Save `RebootRandomService.py` to a desired location, e.g., `C:\RebootRandomService.py`.

3. **Register the service**  
   ```batch
   python C:\RebootRandomService.py install
   ```

4. **Start the service**  
   ```batch
   python C:\RebootRandomService.py start
   ```

## Usage

- The service will automatically start at system boot.
- It will choose a random delay between 10 and 60 minutes, then reboot.
- After reboot, the service restarts and repeats.

## Managing the Service

- **Stop** the service:  
  ```batch
  python C:\RebootRandomService.py stop
  ```
- **Start** the service:  
  ```batch
  python C:\RebootRandomService.py start
  ```
- **Remove** the service:  
  ```batch
  python C:\RebootRandomService.py remove
  ```

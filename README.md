# Random Interval Reboot Service

This Windows Service reboots the computer at random intervals between 10 and 60 minutes.

## Prerequisites
- Administrative privileges

## Installation

0. **Install `uv`**
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

1. **Clone the repo**
   ```batch
   git clone https://github.com/samedit66/reboot_random_service.git
   cd reboot_random_service
   ```

2. **Install dependencies**  
   ```powershell
   uv sync
   ```

3. **Register the service**  
   ```batch
   uv run RebootRandomService.py install
   ```

4. **Start the service**  
   ```batch
   uv run RebootRandomService.py start
   ```

## Usage

- The service will automatically start at system boot.
- It will choose a random delay between 10 and 60 minutes, then reboot.
- After reboot, the service restarts and repeats.

## Managing the Service

- **Stop** the service:  
  ```batch
  uv run RebootRandomService.py stop
  ```
- **Start** the service:  
  ```batch
  uv run RebootRandomService.py start
  ```
- **Remove** the service:  
  ```batch
  uv run RebootRandomService.py remove
  ```

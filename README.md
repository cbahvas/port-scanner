# port-scanner

Simple multithreaded TCP port scanner written in Python.

## Usage

```bash
python scanner.py <host> [--start-port START] [--end-port END] [--timeout SECONDS]
```

Example:

```bash
python scanner.py 127.0.0.1 --start-port 1 --end-port 1024 --timeout 0.3
```

## Disclaimer

Educational use only. Only scan hosts you own or have explicit permission to scan.
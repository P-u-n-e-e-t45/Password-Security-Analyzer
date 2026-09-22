# Password Security Analyzer

A beginner-friendly defensive cybersecurity project written in Python.

## Features
- Password length and character checks
- 12+ character recommendation
- Theoretical entropy calculation
- Local common-password blacklist
- Simple sequential-pattern detection
- Theoretical search-space/crack-time functions
- Console security report
- Unit tests

## Run

### Windows
```powershell
cd Password-Security-Analyzer
python -m app.main
```

If needed:
```powershell
py -m app.main
```

### Linux / Ubuntu
```bash
cd Password-Security-Analyzer
python3 -m app.main
```

## Run Tests
```bash
python -m unittest discover -s tests -v
```

## Project Structure
```text
Password-Security-Analyzer/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── analyzer.py
│   ├── entropy.py
│   ├── patterns.py
│   ├── common_passwords.py
│   ├── crack_time.py
│   └── report.py
├── data/
│   └── common_passwords.txt
├── tests/
│   └── test_analyzer.py

```

## Formula
The theoretical entropy estimate is:

`Entropy = Length × log2(Character Pool)`

Actual security also depends on reuse, predictability, password hashing,
salting, rate limiting, MFA, breach exposure and the attack model.

> This project is for defensive education and local testing. It does not
> attack real accounts or systems.

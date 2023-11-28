# Data Capture lib
Tools for capturing data and get stats from it.

## Requirements
- Python >= 3.11

## How to install

We encourage users to create a virtual env: `<pyhton_binary> -m venv .venv`

Do the following to initialize the environment:
1. Navigate to the project's folder.
2. Run `pip install -r requirements.txt`
3. **Optional**: to install as package run `pip install .`

## How to run tests

1. Navigate to the project's folder.
2. Run `python -m pytest`

## How to use

- `capture.data_capture` -> `DataCapture` : this is the main class that you can use to capture data with the method `add`.
- `capture.stats_builder` -> `StatsBuilder` : this is the class that has the stats methods: `less`, `greater`, `between`.
- You can create your own classes by subclassing the interfaces located in `capture.interfaces`.

### Example

```Python
from capture.data_capture import DataCapture

capture = DataCapture()

capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)

stats = capture.build_stats()

print(stats.less(4))       # should return 2
print(stats.between(3, 6)) # should return 4
print(stats.greater(4))    # should return 2
```

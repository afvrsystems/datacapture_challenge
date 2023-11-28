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

## Algorithm

This package is time-efficient by hashing the captured data to increase the speed of stats operations. The method `add` of `DataCapture` and the methods `less`, `greater`, `between` of `StatsBuilder` have O(1) complexity. This means that no matter how many data is captured, it will take the same time to give a result. The method `build_stats` of `DataCapture` has O(n) complexity, whereby the execution time will increase with a linear behavior respect to the quantity of data.

When analyzing the code it must be taken into account that there aren't O(n) nested operations. The most complex operation inside a O(n) operation must be O(1), and all the operations inside the method should be at most O(n).

The code is based on the following:
* The data is captured using a queue, which is memory-efficient and has O(1) append.
* The hashes are stored in three dictionaries: `histogram`, `less_than_index`, and `greater_than_index`.
* The `histogram` of frequencies has the quantity of appearances of each value in the captured data. First we build a dictionary with keys from 1 to the maximum value in the data, and all the values set to zero. Then it's populated by iterating the data and increasing by 1 respectively.
* The indexes of **lesser values** and **greater values** are populated also by iterating from 1 to the maximum value in the data, but applying the following operations:
    - The `less_than_index` is equal to the additive aggregation of histogram's values. This is possible as the dict-comprehension acts as a sorted iteration increasing by 1, so it keeps the O(n) complexity.
    - The `less_than_index` is shifted by 1 key, so we must substract the `histogram` from it to get the real **less** index.
    - The `greater_than_index` is calculated as the inversion of the `less_than_index`, so it requires the quantity of data minus the `histogram`, minus the `less_than_index`.
* `less`, `greater`, and `between` are retrieved from those indexes, so they have O(1) complexity. The `between` method is calculated by substracting the `greater_than_index` part of both limits of the range to create an intersection, plus the `histogram` value of the upper limit because both the **less** and **greater** indexes are exclusive.

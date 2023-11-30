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

This package is time-efficient by hashing the captured data to increase the speed of stats operations. The method `add` of `DataCapture` and the methods `less`, `greater`, `between` of `StatsBuilder` have ***O(1)*** [time complexity](https://wiki.python.org/moin/TimeComplexity). This means that no matter how many data is captured, it will take the same time to give a result. The method `build_stats` of `DataCapture` has ***O(n)*** complexity, whereby the execution time will increase with a linear behavior respect to the quantity of data.

When analyzing the code it must be taken into account that there aren't ***O(n)*** nested operations. The most complex operation inside a ***O(n)*** operation must be ***O(1)***, and all the operations inside the method should be at most ***O(n)***.

The code is based on the following methods and steps:
- **`DataCapture.add`** method:
    1. The `histogram` that represents the frequency or number of occurrences of some value in all the captured data. It's populated on every `add` call by checking if the new value is present in the dictionary. The corresponding quantity is incremented by 1 if the value is present, otherwise is initialized with 1. This step has ***O(1)*** time complexity because it's an integer comparison and a `dict.get` call.
    2. The `max_value` is initialized as zero, and it's just updated when a new value is greater than it. This step has ***O(1)*** time complexity because it's an integer comparison.
- **`DataCapture.build_stats`** method. This method calls `StatsBuilder.load_data` and passes the arguments `histogram` and `max_value`:
    1. First it clears all the instances variables that are going to be used by the next steps by calling the `clear` method. This is a ***O(1)*** operation as it clears only dictionaries and variables.
    2. Assigns the arguments to their corresponding instance variables.
    3. A for-loop that iterates a range from 1 to `max_value`, including the maximum value. This step has ***O(n)*** time complexity. We have 2 steps with ***O(1)*** complexity inside this loop:
        1. The `less_than_index` assigment, that is equal to the additive aggregation (accumulation) of `histogram`'s values, but shifting to the previous accumulated value. This position offset is achieved by playing with the execution order, so this step must be executed prior to the current `hist_accumulator` addition. This step has ***O(1)*** time complexity because it's just a dict key update.
        2. Add the current histogram value to the hist_accumulator. This operation is ***O(1)*** because both the addition and `dict.get` call are ***O(1)***.
- **`StatsBuilder.less`** method:
    1. The result is calculated by comparing the `value` against `max_value`. If the value is less than the maximum value, it returns its value from `less_than_index`, otherwise returns the maximum value. This has ***O(1)*** complexity, as it's a comparison plus a `dict.get` call.
- **`StatsBuilder.greater`** method:
    1. It's the inverted logic of `StatsBuilder.less` method. The `value` is compared against `max_value` too, but if the value is less than the maximum value, it returns the inverted `less_than_index`, otherwise returns zero. This has ***O(1)*** complexity, as it's a comparison and substraction of two `dict.get` calls.
- **`StatsBuilder.between`** method:
    1. The result is calculated by substracting the `less_than_index` values of both limits of the range, but this was simplified by calling `StatsBuilder.less` method twice. This creates an intersection (something similar to an inner-join), but it's necessary to add the `histogram`'s value of the end (upper) limit because the `StatsBuilder.less` excludes the value used in the comparison. This has ***O(1)*** complexity, as it's a comparison and calls `StatsBuilder.less` that is also ***O(1)***.

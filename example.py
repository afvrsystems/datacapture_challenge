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

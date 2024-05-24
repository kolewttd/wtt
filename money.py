```python
import datetime

class Time:
  def __init__(self):
    self.current_time = datetime.datetime.now()

  def get_current_time(self):
    return self.current_time

  def set_current_time(self, new_time):
    self.current_time = new_time

  def get_time_interval(self, start_time, end_time):
    interval = end_time - start_time
    return interval

  def print_time_interval(self, interval):
    print(interval)

def main():
  time = Time()
  start_time = time.get_current_time()
  # Do something
  end_time = time.get_current_time()
  interval = time.get_time_interval(start_time, end_time)
  time.print_time_interval(interval)

if __name__ == "__main__":
  main()
```

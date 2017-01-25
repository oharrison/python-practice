# NEXT SERVER NUMBER

## Part 1

You're running a pool of servers where the servers are numbered sequentially starting from 1. Over time, any given server might explode, in which case its server number is made available for reuse. When a new server is launched, it should be given the lowest available number.

Write a function which, given the list of currently allocated server numbers, returns the number of the next server to allocate. In addition, you should demonstrate your approach to testing that your function is correct. You may choose to use an existing testing library for your language if you choose, or you may write your own process if you prefer.

For example, your function should behave something like the following:
```
  >> next_server_number([5, 3, 1])
  2
  >> next_server_number([5, 4, 1, 2])
  3
  >> next_server_number([3, 2, 1])
  4
  >> next_server_number([2, 3])
  1
  >> next_server_number([])
  1
```

## Part 2

Server names consist of an alphabetic host type (e.g. "apibox") concatenated with the server number, with server numbers allocated as before (so "apibox1", "apibox2", etc. are valid hostnames).

Write a name tracking class with two operations, `allocate(host_type)` and `deallocate(hostname)`. The former should reserve and return the next available hostname, while the latter should release that hostname back into the pool.

For example:
```
>> tracker = Tracker.new()
>> tracker.allocate("apibox")
"apibox1"
>> tracker.allocate("apibox")
"apibox2"
>> tracker.deallocate("apibox1")
nil
>> tracker.allocate("apibox")
"apibox1"
>> tracker.allocate("sitebox")
"sitebox1"
```

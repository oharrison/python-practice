import next_server_number

class Tracker:
    '''
    Track server names
    '''
    def __init__(self):
        self.hosts = {}

    def allocate(self, host_type):
        '''
        Reserve and return the next available hostname
        '''
        server_number = 1
        if host_type in self.hosts:
            server_number = self._next_server_number(self.hosts[host_type])
            self.hosts[host_type].append(server_number)
        else:
            self.hosts[host_type] = [server_number]
        return host_type + str(server_number)

    def deallocate(self, hostname):
        '''
        Release hostname
        '''
        host_type, server_number = hostname[:-1], int(hostname[-1])
        if host_type in self.hosts:
            self.hosts[host_type].remove(server_number)
        return None

    def _next_server_number(self, server_numbers):
        '''
        Returns the next server number to allocate
        '''
        return next_server_number.next_server_number(server_numbers)

if __name__ == '__main__':
    tracker = Tracker()
    assert tracker.allocate('apibox') == 'apibox1'
    assert tracker.allocate('apibox') == 'apibox2'
    assert tracker.deallocate('apibox1') == None
    assert tracker.allocate('apibox') == 'apibox1'
    assert tracker.allocate('sitebox') == 'sitebox1'
    print('All tests passed.')

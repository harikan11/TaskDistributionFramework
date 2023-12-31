import socket
import threading
import pickle
class MasterServer:
def __init__(self, host='localhost', port=5000):
  self.host = host
  self.port = port
  self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  self.socket.bind((self.host, self.port))
  self.socket.listen(5)
  self.slaves = []
  self.results = []
def start(self):
  print('Master server started on {}:{}'.format(self.host,self.port))
  threading.Thread(target=self.listen_for_slaves).start()
def listen_for_slaves(self):
  while True:
    client, address = self.socket.accept()
    slave = {'client': client, 'address': address}
    self.slaves.append(slave)
    print('New slave registered:', address)
def distribute_task(self, function_name, arguments):
  job = {'function_name': function_name, 'arguments': arguments}
  for slave in self.slaves:
    threading.Thread(target=self.send_job_to_slave,
                     args=(slave, job)).start()
def send_job_to_slave(self, slave, job):
  message = 'EXECUTE:{}:{}'.format(job['function_name'],
                                   pickle.dumps(job['arguments']).decode())
  slave['client'].send(message.encode())
  result = slave['client'].recv(1024).decode()
  self.results.append(pickle.loads(result.encode()))
if __name__ == '__main__':
  server = MasterServer()
  server.start()

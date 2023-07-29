import socket
import threading
import pickle
class SlaveServer:
  def __init__(self, host='localhost', port=5001):
    self.host = host
    self.port = port
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.queue = []
def start(self):
  self.socket.bind((self.host, self.port))
  self.socket.listen(5)
  print('Slave server started on {}:{}'.format(self.host,self.port))
  while True:
    client, address = self.socket.accept()
    client_thread = threading.Thread(target=self.handle_client,args=(client,))
    client_thread.start()
def handle_client(self, client):
  message = client.recv(1024).decode()
  if message.startswith('EXECUTE'):
    function_name, arguments = message.split(':')[1:]
    result = self.execute_function(function_name, arguments)
    client.send(result.encode())
  else:
    print('Invalid message received')
    client.close()
def execute_function(self, function_name, arguments):
  function = getattr(self, function_name)
  args = pickle.loads(arguments.encode())
  result = function(*args)
return pickle.dumps(result).decode()
def add_to_queue(self, function_name, arguments):
  self.queue.append((function_name, arguments))
  self.execute_next_job()
def execute_next_job(self):
  if self.queue:
    function_name, arguments = self.queue.pop(0)
    threading.Thread(target=self.execute_function,args=(function_name, arguments)).start()
if __name__ == '__main__':
  server = SlaveServer()
  server.start()

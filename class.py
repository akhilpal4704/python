class service:
    def __init__(self, service_name, service_port):
        self.service = service_name
        self.port = service_port
        self.isalive = True
    def check_status(self):
        print(f"Checking {self.service} on port {self.port}")
        self.isalive = False
        print(f"Status of {self.service} is {'alive' if self.isalive else 'dead'}")
        return self.isalive

class database(service):
    def __init__(self, service_name, service_port, db_type):
        super().__init__(service_name, service_port)
        self.db_type = db_type
    def dbtype_info(self):
        print(f"{self.service} is a {self.db_type} database running on port {self.port}")
    
s1 = database("HTTP", 80, "SQL")
status = s1.check_status()
print(f"Received status: {status}")
s1.dbtype_info()
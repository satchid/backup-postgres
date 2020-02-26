import gzip
from sh import pg_dump

def generateBackup():
  with gzip.open('postgres.gz', 'wb') as zipFile:
    pg_dump('-h', 'localhost', '-U', 'postgres', 'postgres', _out=zipFile)


if __name__ ==  "__main__":
  generateBackup()
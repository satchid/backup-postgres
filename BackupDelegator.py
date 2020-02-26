import gzip
import delegator

def generateBackup():
  with gzip.open('postgres.gz', 'wb') as zipFile:
    cmd = delegator.run('pg_dump -h localhost -U postgres postgres')
    zipFile.write(cmd.out.encode('utf-8'))

if __name__== "__main__":
   generateBackup()
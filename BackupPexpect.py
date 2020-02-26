import gzip
import pexpect

def generateBackup():
  with gzip.open('postgres.gz', 'wb') as zipFile:
    cmd = pexpect.spawn('pg_dump -h localhost -U postgres postgres')
    zipFile.write(cmd.read())

if __name__== "__main__":
   generateBackup()
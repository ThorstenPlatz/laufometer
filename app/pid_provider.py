import logging
import os


"""
The PidProvider returns the PID of the process which is creating the 
PidProvider instance.

"""
class PidProvider():
	def pid(self):
		return str(os.getpid())
		

"""
Based on the PidProvider this implementation writes a PID file to the current 
working directory. This can be used by shell scripts or other applications to
get the pid of this process.
On deconstruction the PID file will be automatically deleted by the 
PidFileProvider.

"""
class PidFileProvider(PidProvider):
	def __init__(self, pidFilename = None):
		if(pidFilename is None):
			filename = "./pid"
		else:
			filename = pidFilename

		self._pidfile = filename 
		
		
		directory = os.path.dirname(self._pidfile)
		if not os.path.exists(directory):
		    os.makedirs(directory)
		if os.path.isfile(self._pidfile):
			msg = "Pidfile '%s' already exists!" % self._pidfile
			logging.error(msg)
			raise Exception(msg)
		else:
			f = open(self._pidfile, 'wt', encoding='utf-8')
			f.write(self.pid())
			f.close()
			logging.debug("Created pidfile '%s' for PID '%s'" % (self._pidfile, self.pid()) )

	def __del__(self):
		logging.debug("Removing pidfile '%s' for PID '%s'" % (self._pidfile, self.pid()) )
		if os.path.isfile(self._pidfile):
			os.unlink(self._pidfile)
			logging.debug("Removed pidfile '%s' for PID '%s'" % (self._pidfile, self.pid()) )
		else:
			logging.debug("Pidfile '%s' for PID '%s' not found for cleanup." % (self._pidfile, self.pid()) )




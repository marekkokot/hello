
from subprocess import Popen, PIPE
import sys

process = Popen(["./hello"], stdout=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()
if exit_code != 0:
    sys.exit(1)

if "Hello" not in output.decode("utf-8"):
    sys.exit(1)

sys.exit(0)
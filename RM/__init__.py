from subprocess import Popen
import subprocess
import logging


logger = logging.getLogger(__name__)

# Run a command line command and returns stdout


def _run(command):
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, text=True)
    return result.stdout


def _runRemove(command):
    proc = Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    yes_proc = Popen(["yes"], stdout=proc.stdin, text=True)
    proc_output = proc.communicate()[0]
    yes_proc.wait()


def list(repo, length):
    logger.info(repo)
    packageString = _run(["apt", "--installed", "list", "%s*" % repo])
    packageList = packageString.splitlines()
    packageList.pop(0)
    packageNamesWithIndex = []
    for names in packageList:
        logger.debug("Package: " + names)
        index = packageList.index(names) + 1
        packageNamesWithIndex.append(str(index) + " -> " + names.strip())
        if index == int(length):
            break
    return packageNamesWithIndex


def remove(package, extension):
    type_remove = extension.preferences["type-remove"]
    result = _runRemove(["pkexec", "apt", type_remove, package.split("->")[1].strip().split("/")[0]])
    print(result)

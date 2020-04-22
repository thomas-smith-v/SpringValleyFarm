from subprocess import Popen, PIPE
import psutil

def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index(b'=') + 1:output.rindex(b"'")])

def get_core_voltage():
    process = Popen(['vcgencmd', 'measure_volts', 'core'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index(b'=') + 1:output.rindex(b"V")])

def get_cpu_percent():
    return psutil.cpu_percent()

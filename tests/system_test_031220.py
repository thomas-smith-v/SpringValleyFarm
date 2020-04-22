from src import system_info, metrics

def test():
    cpu_temperature = system_info.get_cpu_temperature()
    core_voltage = system_info.get_core_voltage()
    cpu_percent = system_info.get_cpu_percent()

    metrics.post_system_metric(name="cpu_temperature", value=cpu_temperature)
    metrics.post_system_metric(name="core_voltage", value=core_voltage)
    metrics.post_system_metric(name="cpu_percent", value=cpu_percent)


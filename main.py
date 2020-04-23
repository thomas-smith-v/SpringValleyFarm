import schedule
import time
import tests.system_test_031220 as t
from src import weather_info, system_info, metrics

def run_system_metrics():
    cpu_temperature = system_info.get_cpu_temperature()
    core_voltage = system_info.get_core_voltage()
    cpu_percent = system_info.get_cpu_percent()

    metrics.post_system_metric(name="cpu_temperature", value=cpu_temperature)
    metrics.post_system_metric(name="core_voltage", value=core_voltage)
    metrics.post_system_metric(name="cpu_percent", value=cpu_percent)
    print("\n")

def run_weather_metrics():
    weather = weather_info.get_weather()
    
    temperature_forecast = weather_info.get_temperature_forecast(weather)
    sky_cover_forecast = weather_info.get_sky_cover_forecast(weather)

    current_temperature = weather_info.get_current(temperature_forecast)
    current_sky_cover = weather_info.get_current(sky_cover_forecast)

    metrics.post_weather_metric(name="current_temperature", value=current_temperature)
    metrics.post_weather_metric(name="current_sky_cover", value=current_sky_cover)
    
    """
    ~~ Unable to upload this data to Splunk. This is supposed to upload the       ~~
    ~~ 7-day forecast for temperature and sky cover to be shown on the dashboard. ~~
    
    metrics.post_weather_metric(name="temperature_forecast", value=temperature_forecast)
    metrics.post_weather_metric(name="sky_cover_forecast", value=sky_cover_forecast)

    """
    print("\n")
    

def main():
    # Initial upload
    run_system_metrics()
    run_weather_metrics()

    # Schedule future uploads
    schedule.every(5).minutes.do(run_system_metrics)
    schedule.every(1).hour.do(run_weather_metrics)
    
    # Main loop
    while True:
        schedule.run_pending()
        time.sleep(0.2)

if __name__ == "__main__":
    main()

# WeatherFM

A Raspberry Pi weather repeater using Geonames, Open Weather Map and GTTS to generate audio weather reports from random locations.

## Dependencies

This relys on [PiRate Radio](https://github.com/Make-Magazine/PirateRadio) following the accompanying tutorial found at [Make Projects](https://makezine.com/projects/raspberry-pirate-radio/).

## Setup

Install Python modules:
```
pip install -r requirements.txt
```

Rename ```.env.example``` to ```.env``` and populate with the required API keys:
```
WEATHER_KEY={Open Weather Map key}
LOCATION_KEY={Geonames key}
```

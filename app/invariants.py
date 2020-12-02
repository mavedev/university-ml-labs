from typing import Union


class Constants:
    TITLES = [
        'Pressure',
        'Temperature',
        'Temperature in Kelvin',
        'Temperature (dew point)',
        'Relative Humidity',
        'Saturation vapor pressure',
        'Vapor pressure',
        'Vapor pressure deficit',
        'Specific humidity',
        'Water vapor concentration',
        'Airtight',
        'Wind speed',
        'Maximum wind speed',
        'Wind direction in degrees',
    ]

    FEATURE_KEYS = [
        'p (mbar)',
        'T (degC)',
        'Tpot (K)',
        'Tdew (degC)',
        'rh (%)',
        'VPmax (mbar)',
        'VPact (mbar)',
        'VPdef (mbar)',
        'sh (g/kg)',
        'H2OC (mmol/mol)',
        'rho (g/m**3)',
        'wv (m/s)',
        'max. wv (m/s)',
        'wd (deg)',
    ]

    COLORS = [
        'red',
        'orange',
        'yellow',
        'green',
        'cyan',
        'blue',
        'pink'
    ]

    DATE_TIME_KEY = 'Date Time'


class Types:
    Path = Union[str]

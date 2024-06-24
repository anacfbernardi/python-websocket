from src.commons.base_enum import BaseEnum


class ConfigurationCommandsType(BaseEnum):
    ADD_TRADING_AGGREGATOR = "add-trading-aggregator"
    CLEAR_TRADING_AGGREGATORS = "clear-trading-aggregators"
    ADD_PROVIDER = "add-provider"
    CLEAR_PROVIDERS = "clear-providers"
    CLEAR_PRICES = "clear-prices"

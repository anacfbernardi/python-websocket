async def get_symbols():
    symbols = []

    from src.providers.providers_controller import providers

    for provider in providers.get_providers():
        symbols.extend(provider.symbols)

    return symbols

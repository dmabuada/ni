def active_gateways():
    """Get a list of activated payment gateways, in the form of
    [(module, config module name),...]
    """
    from django.apps.registry import apps
    gateways = []
    for app in apps.get_apps():
        if hasattr(app, 'PAYMENT_PROCESSOR'):
            parts = app.__name__.split('.')[:-1]
            module = ".".join(parts)
            group = 'PAYMENT_%s' % parts[-1].upper()
            gateways.append((module, group))
    return gateways

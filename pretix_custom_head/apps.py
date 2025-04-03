from django.utils.translation import gettext_lazy as _
from pretix.base.plugins import PluginConfig
from django.conf import settings
from . import __version__


class PluginApp(PluginConfig):
    name = "pretix_custom_head"
    verbose_name = _("Custom Head Injection & Plausible Tracking")

    class PretixPluginMeta:
        name = _("Custom html head injection & Plausible Tracking")
        author = "Bergruebe"
        description = _("Fügt beliebigen Code in den <head> ein und trackt Bestellungen mit Plausible Analytics.")
        visible = True
        version = __version__
        compatibility = "pretix>=4.0.0"

    def ready(self):
        plausible_url = settings.CONFIG_FILE.get("custom_head", "plausible_url", fallback=None)
        if plausible_url:
            # Add Plausible Analytics domain to CSP settings
            settings.CSP_SCRIPT_SRC += (plausible_url,)
        from . import signals  # noqa
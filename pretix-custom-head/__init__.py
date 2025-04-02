from django.utils.translation import gettext_lazy as _
from pretix.base.plugins import PluginConfig


class PluginApp(PluginConfig):
    name = "pretix_custom_head_tracking"
    verbose_name = _("Custom Head Injection & Plausible Tracking")

    class PretixPluginMeta:
        name = _("Custom Head Injection & Plausible Tracking")
        author = "Dein Name"
        description = _("Fügt beliebigen Code in den <head> ein und trackt Bestellungen mit Plausible Analytics.")
        visible = True
        version = "1.0.0"
        compatibility = "pretix>=4.0.0"

default_app_config = "pretix_custom_head_tracking.PluginApp"
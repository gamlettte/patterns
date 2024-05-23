class UIConfiguration:
    def __init__(self, theme=None, widgets=None, layout=None, notifications_enabled=False):
        self.theme = theme
        self.widgets = widgets if widgets is not None else []
        self.layout = layout
        self.notifications_enabled = notifications_enabled

    def __str__(self):
        return (f"UIConfiguration(theme={self.theme}, widgets={self.widgets}, "
                f"layout={self.layout}, notifications_enabled={self.notifications_enabled})")

if __name__ == "__main__":
    ui_config = UIConfiguration(theme="Dark",
                                widgets=["Weather", "News"],
                                layout="Grid",
                                notifications_enabled=True)

    print(ui_config)


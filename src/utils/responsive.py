def get_dims(page):
    """Returns dimension values scaled to the current window width."""
    w = page.window.width
    if not isinstance(w, (int, float)) or w <= 0:
        w = 800
    s = max(0.5, min(1.25, w / 800))
    return {
        "image_lg": int(120 * s),          # home page avatar
        "image_sm": int(80 * s),           # about page avatar
        "title_size": int(32 * s),         # large page titles
        "heading_size": int(28 * s),       # medium headings
        "subtext_size": int(18 * s),       # subtitle / callout text
        "padding": int(30 * s),            # container padding
        "spacing": int(20 * s),            # column spacing
        "field_width": min(300, w * 0.75), # form field width
        "tab_h_padding": int(40 * s),      # tab bar horizontal padding
    }

"""
Constructs themes/selenized.json

Notes:
- Transparency is supported, just append to hex (e.g. `80` for 50%)
- More info:
  - https://zed.dev/docs/themes
  - https://zed.dev/docs/extensions/themes
  - https://zed.dev/schema/themes/v0.2.0.json
"""

import json

# ── Selenized palettes (sRGB hex from the-values.md) ─────────────────────────

selenized_dark_colors = {
    "bg_0": "#103c48",
    "bg_1": "#184956",
    "bg_2": "#2d5b69",
    "dim_0": "#72898f",
    "fg_0": "#adbcbc",
    "fg_1": "#cad8d9",
    "red": "#fa5750",
    "green": "#75b938",
    "yellow": "#dbb32d",
    "blue": "#4695f7",
    "magenta": "#f275be",
    "cyan": "#41c7b9",
    "orange": "#ed8649",
    "violet": "#af88eb",
    "br_red": "#ff665c",
    "br_green": "#84c747",
    "br_yellow": "#ebc13d",
    "br_blue": "#58a3ff",
    "br_magenta": "#ff84cd",
    "br_cyan": "#53d6c7",
    "br_orange": "#fd9456",
    "br_violet": "#bd96fa",
}

selenized_black_colors = {
    "bg_0": "#181818",
    "bg_1": "#252525",
    "bg_2": "#3b3b3b",
    "dim_0": "#777777",
    "fg_0": "#b9b9b9",
    "fg_1": "#dedede",
    "red": "#ed4a46",
    "green": "#70b433",
    "yellow": "#dbb32d",
    "blue": "#368aeb",
    "magenta": "#eb6eb7",
    "cyan": "#3fc5b7",
    "orange": "#e67f43",
    "violet": "#a580e2",
    "br_red": "#ff5e56",
    "br_green": "#83c746",
    "br_yellow": "#efc541",
    "br_blue": "#4f9cfe",
    "br_magenta": "#ff81ca",
    "br_cyan": "#56d8c9",
    "br_orange": "#fa9153",
    "br_violet": "#b891f5",
}

selenized_light_colors = {
    "bg_0": "#fbf3db",
    "bg_1": "#ece3cc",
    "bg_2": "#d5cdb6",
    "dim_0": "#909995",
    "fg_0": "#53676d",
    "fg_1": "#3a4d53",
    "red": "#d2212d",
    "green": "#489100",
    "yellow": "#ad8900",
    "blue": "#0072d4",
    "magenta": "#ca4898",
    "cyan": "#009c8f",
    "orange": "#c25d1e",
    "violet": "#8762c6",
    "br_red": "#cc1729",
    "br_green": "#428b00",
    "br_yellow": "#a78300",
    "br_blue": "#006dce",
    "br_magenta": "#c44392",
    "br_cyan": "#00978a",
    "br_orange": "#bc5819",
    "br_violet": "#825dc0",
}

selenized_white_colors = {
    "bg_0": "#ffffff",
    "bg_1": "#ebebeb",
    "bg_2": "#cdcdcd",
    "dim_0": "#878787",
    "fg_0": "#474747",
    "fg_1": "#282828",
    "red": "#d6000c",
    "green": "#1d9700",
    "yellow": "#c49700",
    "blue": "#0064e4",
    "magenta": "#dd0f9d",
    "cyan": "#00ad9c",
    "orange": "#d04a00",
    "violet": "#7f51d6",
    "br_red": "#bf0000",
    "br_green": "#008400",
    "br_yellow": "#af8500",
    "br_blue": "#0054cf",
    "br_magenta": "#c7008b",
    "br_cyan": "#009a8a",
    "br_orange": "#ba3700",
    "br_violet": "#6b40c3",
}


def build_palette(base):
    """Convert raw selenized hex map into the dict the theme builder expects."""
    return {
        # Background layers (darkest → lighter)
        "bg1": base["bg_0"],
        "bg2": base["bg_2"],
        # Foreground layers
        "fg1": base["fg_0"],
        "fg2": base["dim_0"],
        "fg3": base["fg_1"],
        # Accent hues
        "red": base["red"],
        "green": base["green"],
        "yellow": base["yellow"],
        "blue": base["blue"],
        "magenta": base["magenta"],
        "cyan": base["cyan"],
        "orange": base["orange"],
        "violet": base["violet"],
        # Bright accent hues
        "br_red": base["br_red"],
        "br_green": base["br_green"],
        "br_yellow": base["br_yellow"],
        "br_blue": base["br_blue"],
        "br_magenta": base["br_magenta"],
        "br_cyan": base["br_cyan"],
        "br_orange": base["br_orange"],
        "br_violet": base["br_violet"],
    }


def selenized_theme(p):
    accents = [p["blue"]]
    players = [
        {
            "background": p[color],
            "cursor": p[color],
            "selection": p[color] + "66",
        }
        for color in [
            "blue",
            "cyan",
            "green",
            "magenta",
            "orange",
            "red",
            "violet",
            "yellow",
        ]
    ]
    syntax = {
        "attribute": {"color": p["blue"]},
        "boolean": {"color": p["yellow"]},
        "comment": {"color": p["fg2"], "font_style": "italic"},
        "comment.doc": {"color": p["fg2"], "font_style": "italic"},
        "constant": {"color": p["cyan"]},
        "constructor": {"color": p["blue"]},
        "embedded": {"color": p["fg1"]},
        "emphasis": {"color": p["blue"]},
        "emphasis.strong": {"color": p["blue"], "font_weight": 700},
        "enum": {"color": p["orange"]},
        "function": {"color": p["blue"]},
        "hint": {
            "color": p["fg2"] + "ff",
            "font_weight": 700,
        },
        "keyword": {"color": p["green"]},
        "label": {"color": p["blue"]},
        "link_text": {"color": p["blue"], "font_style": "italic"},
        "link_uri": {"color": p["violet"]},
        "number": {"color": p["magenta"]},
        "operator": {"color": p["green"]},
        "predictive": {
            "background_color": p["bg1"],
            "color": p["magenta"],
        },
        "preproc": {"color": p["orange"]},
        "primary": {"color": p["fg1"]},
        "property": {"color": p["blue"]},
        "punctuation": {"color": p["fg2"]},
        "punctuation.bracket": {"color": p["fg2"]},
        "punctuation.delimiter": {"color": p["fg2"]},
        "punctuation.list_marker": {"color": p["fg2"]},
        "punctuation.special": {"color": p["fg2"]},
        "string": {"color": p["cyan"]},
        "string.escape": {"color": p["fg2"]},
        "string.regex": {"color": p["orange"]},
        "string.special": {"color": p["orange"]},
        "string.special.symbol": {"color": p["orange"]},
        "tag": {"color": p["red"]},
        "text.literal": {"color": p["cyan"]},
        "title": {"color": p["orange"], "font_weight": 700},
        "type": {"color": p["yellow"]},
        "variable": {"color": p["fg1"]},
        "variant": {"color": p["blue"]},
    }
    theme = {
        "accents": accents,
        "background": p["bg1"],
        "background.appearance": "transparent",
        "border": p["fg2"],
        "border.disabled": None,
        "border.focused": p["fg1"],
        "border.selected": p["blue"],
        "border.transparent": None,
        "border.variant": None,
        "conflict": p["red"],
        "conflict.background": p["bg1"],
        "conflict.border": p["red"],
        "created": p["green"],
        "created.background": p["bg1"],
        "created.border": p["green"],
        "deleted": p["orange"],
        "deleted.background": p["bg1"],
        "deleted.border": p["orange"],
        "drop_target.background": p["bg2"],
        "editor.active_line.background": p["bg2"],
        "editor.active_line_number": p["fg1"],
        "editor.active_wrap_guide": p["fg2"],
        "editor.background": p["bg1"],
        "editor.document_highlight.bracket_background": p["blue"] + "66",
        "editor.document_highlight.read_background": p["blue"] + "33",
        "editor.document_highlight.write_background": p["blue"] + "33",
        "editor.foreground": p["fg1"],
        "editor.gutter.background": p["bg1"],
        "editor.highlighted_line.background": p["bg1"],
        "editor.indent_guide": p["bg2"],
        "editor.indent_guide_active": p["fg2"],
        "editor.invisible": p["bg2"],
        "editor.line_number": p["fg2"],
        "editor.subheader.background": p["bg1"],
        "editor.wrap_guide": p["bg2"],
        "element.active": p["bg2"],
        "element.background": p["bg2"],
        "element.disabled": p["bg2"],
        "element.hover": p["bg2"],
        "element.selected": p["blue"] + "66",
        "elevated_surface.background": p["bg1"],
        "error": p["red"],
        "error.background": p["bg1"],
        "error.border": p["red"],
        "ghost_element.active": p["fg1"],
        "ghost_element.background": p["bg2"],
        "ghost_element.disabled": p["fg2"],
        "ghost_element.hover": p["blue"] + "66",
        "ghost_element.selected": p["blue"] + "66",
        "hidden": p["fg2"],
        "hidden.background": p["bg1"],
        "hidden.border": p["bg1"],
        "hint": p["fg2"] + "AA",
        "hint.background": p["bg1"] + "00",
        "hint.border": p["fg2"],
        "icon": p["fg1"],
        "icon.accent": accents[0],
        "icon.disabled": p["fg2"],
        "icon.muted": p["fg2"],
        "icon.placeholder": p["fg2"],
        "ignored": p["fg2"],
        "ignored.background": p["bg1"],
        "ignored.border": p["fg2"],
        "info": p["blue"],
        "info.background": p["bg1"],
        "info.border": p["blue"],
        "link_text.hover": p["blue"],
        "modified": p["yellow"],
        "modified.background": p["bg1"],
        "modified.border": p["yellow"],
        "pane.focused_border": p["blue"],
        "pane_group.border": p["fg1"],
        "panel.background": p["bg2"],
        "panel.focused_border": p["blue"],
        "panel.indent_guide": p["fg2"],
        "panel.indent_guide_active": p["fg1"],
        "panel.indent_guide_hover": p["fg3"],
        "players": players,
        "predictive": p["magenta"],
        "predictive.background": p["bg1"] + "00",
        "predictive.border": p["magenta"],
        "renamed": p["magenta"],
        "renamed.background": p["bg1"] + "00",
        "renamed.border": p["magenta"],
        "scrollbar.thumb.background": p["bg2"] + "BB",
        "scrollbar.thumb.border": None,
        "scrollbar.thumb.hover_background": p["bg2"],
        "scrollbar.track.background": None,
        "scrollbar.track.border": p["bg2"],
        "search.match_background": p["yellow"] + "99",
        "status_bar.background": p["bg2"],
        "success": p["green"],
        "success.background": p["bg1"] + "00",
        "success.border": p["green"],
        "surface.background": p["bg1"],
        "syntax": syntax,
        "tab.active_background": p["bg1"],
        "tab.inactive_background": p["bg2"],
        "tab_bar.background": p["bg2"],
        "terminal.ansi.background": p["bg1"],
        "terminal.ansi.black": p["bg2"],
        "terminal.ansi.blue": p["blue"],
        "terminal.ansi.bright_black": p["bg1"],
        "terminal.ansi.bright_blue": p["br_blue"],
        "terminal.ansi.bright_cyan": p["br_cyan"],
        "terminal.ansi.bright_green": p["br_green"],
        "terminal.ansi.bright_magenta": p["br_magenta"],
        "terminal.ansi.bright_red": p["br_red"],
        "terminal.ansi.bright_white": p["fg3"],
        "terminal.ansi.bright_yellow": p["br_yellow"],
        "terminal.ansi.cyan": p["cyan"],
        "terminal.ansi.dim_black": p["bg2"],
        "terminal.ansi.dim_blue": p["blue"],
        "terminal.ansi.dim_cyan": p["cyan"],
        "terminal.ansi.dim_green": p["green"],
        "terminal.ansi.dim_magenta": p["magenta"],
        "terminal.ansi.dim_red": p["red"],
        "terminal.ansi.dim_white": p["fg1"],
        "terminal.ansi.dim_yellow": p["yellow"],
        "terminal.ansi.green": p["green"],
        "terminal.ansi.magenta": p["magenta"],
        "terminal.ansi.red": p["red"],
        "terminal.ansi.white": p["fg3"],
        "terminal.ansi.yellow": p["yellow"],
        "terminal.background": p["bg1"],
        "terminal.bright_foreground": p["fg3"],
        "terminal.dim_foreground": p["fg2"],
        "terminal.foreground": p["fg1"],
        "text": p["fg1"],
        "text.accent": accents[0],
        "text.disabled": p["fg2"],
        "text.muted": p["fg2"],
        "text.placeholder": p["fg2"],
        "title_bar.background": p["bg2"],
        "title_bar.inactive_background": p["bg2"],
        "toolbar.background": p["bg1"],
        "unreachable": p["violet"],
        "unreachable.background": p["bg1"],
        "unreachable.border": p["violet"],
        "warning": p["orange"],
        "warning.background": p["bg1"],
        "warning.border": p["orange"],
    }
    return theme


# ── Build all four themes ────────────────────────────────────────────────────

selenized_dark = {
    "appearance": "dark",
    "name": "Selenized Dark",
    "style": selenized_theme(build_palette(selenized_dark_colors)),
}
print("Added Selenized Dark")

selenized_black = {
    "appearance": "dark",
    "name": "Selenized Black",
    "style": selenized_theme(build_palette(selenized_black_colors)),
}
print("Added Selenized Black")

selenized_light = {
    "appearance": "light",
    "name": "Selenized Light",
    "style": selenized_theme(build_palette(selenized_light_colors)),
}
print("Added Selenized Light")

selenized_white = {
    "appearance": "light",
    "name": "Selenized White",
    "style": selenized_theme(build_palette(selenized_white_colors)),
}
print("Added Selenized White")

selenized_dict = {
    "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
    "author": "harmtemolder",
    "name": "Selenized",
    "themes": [
        selenized_dark,
        selenized_black,
        selenized_light,
        selenized_white,
    ],
}

json_file = "themes/selenized.json"
try:
    with open(json_file, "w") as f:
        json.dump(selenized_dict, f, indent=2)
        print(f"Wrote to {json_file}")
except OSError as e:
    print(f"Error writing {json_file}: {e}")
    raise

import json
import pathlib
import re
import sys

PATH = pathlib.Path(__file__).parent
PATH_THEME = PATH / ".." / "SolarDim" / "resources" / "theme"


def main():
    # Load colors from `colors.json` into dictionary
    with open(PATH / "colors.json", "r", encoding="utf-8") as f_in:
        colors = json.load(f_in)

    # ---
    # Replace all {{colorname}} in `SolarDim.theme.json` and save it in `SolarDim/resources/theme`

    with open(PATH / "SolarDim.theme.json", "r", encoding="utf-8") as f_in:
        theme = f_in.read()

    def replacer(match):
        key = match.group(1)
        if key in colors:
            return colors[key]
        print(f"[!] Key {key} does not exist.", file=sys.stderr)
        input()
        return "#000000"

    result = re.sub(r"{{(\w+)}}", replacer, theme)
    result_dict = json.loads(result)

    with open(PATH_THEME / "SolarDim.theme.json", "w", encoding="utf-8") as f_out:
        json.dump(result_dict, f_out, indent=4, ensure_ascii=False)

    # ---
    # Replace all {{colorname}} in `scheme.xml` (this time color codes are without `#`) and save it in `SolarDim/resources/theme`

    with open(PATH / "scheme.xml", "r", encoding="utf-8") as f_in:
        scheme = f_in.read()

    def replacer2(match):
        key = match.group(1)
        if key in colors:
            return colors[key][1:]
        print(f"[!] Key {key} does not exist.", file=sys.stderr)
        input()
        return "000000"

    result = re.sub(r"{{(\w+)}}", replacer2, scheme)

    with open(PATH_THEME / "scheme.xml", "w", encoding="utf-8") as f_out:
        f_out.write(result)


if __name__ == "__main__":
    main()    
    print("ok")

# Terminal Colors

With this repository, you can add different colors to python scripts that output text. When you run the script in a terminal, you will see all the colors applied to the text (some text editor's support colored text as well).

## Installation

Clone this repository into your project directory.

```bash
git clone https://github.com/Zemelware/Terminal-Colors.git
```

## Usage

Drag "TerminalColors.py" into the same folder as your python script, then import it into your script.

```py
from TerminalColors import *
```

Use the "printColor" function to print text that can be stylized with color and other styles (eg. bold, italics, etc.)

```py
printColor(text, *styles)
```

The first argument is the text you want to output. The second argument is all the styles you want applied to the text, comma separated (there is no order you need to follow, just list all the styles). The styles are all capitalized. To see all the styles that you can use, look at TerminalColors.py. Also, if you use conflicting styles (eg. RED and BLUE) then the last one you specify will be applied.

## Examples

```py
printColor("Hello World!", GREEN, BOLD, UNDERLINE)
```

```py
printColor("Foo Bar", BLINK, RED, INVERT, UNDERLINE)
```

## Contributing

Pull requests are welcome. If you want add more ANSI color codes to the main python file, that would be very helpful.

## License

This project is licensed under the MIT License - look at the [LICENSE.md]("https://github.com/Zemelware/Terminal-Colors/blob/master/LICENSE") file for details

# Ulauncher Timestamp

> [ulauncher](https://ulauncher.io/) Extension to convert timestamp date to human readable date.

## Usage

![demo](demo.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/brpaz/ulauncher-timestamp```

## Settings

Output formatting settings use [strftime](https://strftime.org/).  Please refer to the official documentation for proper values.

Default: `%Y-%m-%d %H:%M:%S`

## Development

```git
git clone https://github.com/brpaz/ulauncher-timestamp
cd ~/.cache/ulauncher_cache/extensions/ulauncher-timestamp
ln -s <repo_location> ulauncher-timestamp
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## License

MIT

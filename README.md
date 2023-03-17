
# Svelte Jupyter Widget Example

This is an updated example of using Svelte in a custom Jupyter widget. It was created from [widget-ts-cookiecutter](https://github.com/jupyter-widgets/widget-ts-cookiecutter). For an older example, see [widget-svelte-cookiecutter](https://github.com/cabreraalex/widget-svelte-cookiecutter).

## Development Installation

Create a dev environment:
```bash
conda create -n svelte_widget -c conda-forge nodejs yarn python jupyterlab
conda activate svelte_widget
```

Install the python. This will also build the TS package.
```bash
pip install -e ".[test, examples, dev]"
```

When developing your extensions, you need to manually enable your extensions with the
notebook / lab frontend. For lab, this is done by the command:

```
jupyter labextension develop --overwrite .
jlpm run build
```

For classic notebook, you need to run:

```
jupyter nbextension install --sys-prefix --symlink --overwrite --py svelte_widget
jupyter nbextension enable --sys-prefix --py svelte_widget
```

Note that the `--symlink` flag doesn't work on Windows, so you will here have to run
the `install` command every time that you rebuild your extension. For certain installations
you might also need another flag instead of `--sys-prefix`, but we won't cover the meaning
of those flags here.

### How to see your changes
#### Typescript:
Watch the source directory and run Jupyter lab or notebook at the same time in different
terminals to watch for changes in the extension's source and automatically rebuild the widget.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm run watch
# Run JupyterLab in another terminal
jupyter lab
```

After a change wait for the build to finish and then refresh your browser and the changes should take effect.

#### Python:
If you make a change to the python code then you will need to restart the notebook kernel to have it take effect.

### VSCode Setup

The following extensions are useful when developing in [VSCode](https://code.visualstudio.com):

- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
- [Prettier]https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [Svelte for VS Code](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode)

`.vscode/settings.json` contains modified settings for linting and formatting code. You will need to update the pylint, python, and node paths in this file.

## Updating the version

To update the version, install tbump and use it to bump the version.
By default it will also create a tag.

```bash
pip install tbump
tbump <new-version>
```

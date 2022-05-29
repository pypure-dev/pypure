# pypure.core

## Functions
```py
def init(
    config: bool = True,
    config_path: Union[str, Path] = config.default,
) -> None
```
&emsp;Initializes pypure and it's components.

<h3>&emsp;Args</h3>
&emsp;&emsp;<b>config</b>: bool = True

&emsp;&emsp;&emsp;Tells if the config file should be used.

&emsp;&emsp;<b>config_path</b>: Union[str, Path] = ...

&emsp;&emsp;&emsp;The config file path to be used.

<h3>&emsp;Returns</h3>
&emsp;&emsp;<b>None</b>
<h3>&emsp;Raises</h3>
&emsp;&emsp;<b>None</b>

```py
def quit() -> None
```
&emsp;Uninitializes pypure and it's components.
<h3>&emsp;Args</h3>
&emsp;&emsp;<b>None</b>
<h3>&emsp;Returns</h3>
&emsp;&emsp;<b>None</b>
<h3>&emsp;Raises</h3>
&emsp;&emsp;<b>None</b>

## Variables
```py
debug = None
```
&emsp;True if you want to have Pure print logs and debugs in the stream.

```py
config = configparser.ConfigParser()
```
&emsp;The configuration of PyPure.

```py
pygame = builtins.Module("pygame")
```
&emsp;The pygame library.

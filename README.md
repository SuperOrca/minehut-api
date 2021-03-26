# 📦 Minehut Python

### An API wrapper for the minehut API.

## 🔧 Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the main branch.

```bash
pip install git+https://github.com/SuperOrca/minehut-api.git
```

## 📌 Usage

To import, use `minehut`
```python
import minehut
```

Example:
```python
import minehut
# Retrieving the Minehut server through its name
server = minehut.getServer("Elestra")
# Printing all the plugin names inside the server
print([plugin.getName() for plugin in server.getPlugins()])
```

## ➕ Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## 📄 Sources
1. [api.bennydoesstuff.me](https://api.bennydoesstuff.me/)
2. [honkling](https://github.com/honkling/Minehut-API-Docs)

## License
[MIT](https://choosealicense.com/licenses/mit/)


- créer env virtuel
- ajouter un .gitignore
- https://playwright.dev/python/docs/intro
- vscode python extension
- sur volet test, run tests with pytest
- créer pytest.ini avec --headed


voir ce qu'il y a derrière **Playwright CLI** et **Playwright MCP**
ici https://playwright.dev/python/

voir aussi codegen : https://playwright.dev/python/docs/codegen-intro

voir aussi **Run tests in parallel** 
in https://playwright.dev/python/docs/running-tests

explain file structure
give process to create or checkout a project


## setup

https://playwright.dev/python/docs/intro
https://docs.astral.sh/uv/

```
git clone pw-training
cd pw-training
uv init .
uv add pytest-playwright
uv run playwright install

```

Create `tests/test_example.py` (https://playwright.dev/python/docs/intro#add-example-test)

```
uv run pytest
```

install Microsoft's **Python** vs code plugin (install automatically 3 other extensions)

create pytest.ini

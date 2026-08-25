


- https://playwright.dev/python/docs/intro
- vscode python extension
- sur volet test, run tests with pytest
- créer pytest.ini avec --headed
- comment garder le navigateur ouvert à la fin d'un test https://chat.mistral.ai/work/c8ff1542-7044-49b1-a83f-1cd65ee85adc


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
uv add pytest-rerunfailures
uv run playwright install

```

Create `tests/test_example.py` (https://playwright.dev/python/docs/intro#add-example-test)

```
uv run pytest
```

install Microsoft's **Python** vs code plugin (install automatically 3 other extensions)

create pytest.ini


page.pause() -- keeps the browser open, gives access to recorder and pick locator


page objects :
https://playwright.dev/python/docs/pom
pom custom fixtures :
https://chat.mistral.ai/work/8153763d-ded5-479c-afe2-821b5be1cc0e


idées :
on a vu qu'il est compliqué d'attaquer "tout seul" le test sur le login.
C'est peut-être plus simple si on attaque ce test juste après le login, en zappant la partie théorique.
quitte à ne pas appliqer toutes les bonnes pratiques... 
ajouter de la sémantique sur le dom ?

next step :
créer les test en utilisant le recorder pour une première version
tant mieux si le résultat n'est pas fou
on fera une étape d'amélioration / refactor page object

méthodo :
écrire en texte le test qu'on veut faire
ensuite l'exécuter avec le recorder ou l'ia

quels param pour lancer les tests en parallèle (nombre de worker ?)

comment lancer un sous ensemble de tests
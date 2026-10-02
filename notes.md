


- sur volet test, run tests with pytest
- comment garder le navigateur ouvert à la fin d'un test https://chat.mistral.ai/work/c8ff1542-7044-49b1-a83f-1cd65ee85adc


voir ce qu'il y a derrière **Playwright CLI** et **Playwright MCP**
ici https://playwright.dev/python/

voir aussi codegen : https://playwright.dev/python/docs/codegen-intro

voir aussi **Run tests in parallel** 
in https://playwright.dev/python/docs/running-tests

explain file structure
give process to create or checkout a project


## setup

uv : how to create .venv from pyproject.toml ?

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

comment lancer un sous ensemble de tests
voir la gestion des "marks" : https://chat.mistral.ai/work/f300265c-91dc-492a-9751-3ef1e08bef25
mais il y a peut-être une autre méthode

sync or async api ?
https://chat.mistral.ai/work/f300265c-91dc-492a-9751-3ef1e08bef25
=> always use the sync api, except when you need to wait for two events...


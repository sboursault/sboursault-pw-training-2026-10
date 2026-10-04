# pytest-playwright native fixtures

Source: `.venv/lib/python3.12/site-packages/pytest_playwright/pytest_playwright.py`

| Fixture | Scope | Type | Purpose |
|---|---|---|---|
| `page` | function | `Page` | Ready-to-use page for the current test |
| `context` | function | `BrowserContext` | Browser context for the current test |
| `new_context` | function | callback | Create additional contexts (`new_context(locale="de-DE")`), auto-closed at teardown |
| `browser` | session | `Browser` | Launched browser instance |
| `playwright` | session | `Playwright` | The Playwright driver object |
| `browser_type` | session | `BrowserType` | Browser type for the current browser |
| `launch_browser` | session | callback | Overridable browser-launch callback |
| `connect_options` | session | `dict \| None` | Options for connect mode |
| `browser_name` | session | `str \| None` | Current browser name, e.g. `"chromium"` |
| `browser_channel` | session | `str \| None` | From `--browser-channel` |
| `browser_type_launch_args` | session | `dict` | Base kwargs passed to `browser_type.launch()` |
| `browser_context_args` | session | `dict` | Base kwargs passed to `browser.new_context()`, override to customize locale, timezone, etc. |
| `device` | session | `str \| None` | From `--device` |
| `is_webkit` | session | `bool` | True when running WebKit |
| `is_firefox` | session | `bool` | True when running Firefox |
| `is_chromium` | session | `bool` | True when running Chromium |
| `output_path` | function | `str` | Per-test output directory path |
| `delete_output_dir` | session (autouse) | - | Cleans the output directory |
| `_pw_artifacts_folder` | session | internal | Artifacts temp folder plumbing |
| `_artifacts_recorder` | function | internal | Records traces, videos and screenshots |

Related marker (not a fixture): `@pytest.mark.browser_context_args(**kwargs)` adds per-test arguments to `browser.new_context()`.

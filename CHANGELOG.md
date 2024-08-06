# CHANGELOG

## v0.1.0-rc.9 (2024-08-06)

### Feature

* feat: Nixify (#37)

* feat: Add nix flake with python and dependencies

* docs: Update flake documentation

* Restore correct lockfile

---------

Co-authored-by: nohr-ai &lt;oyvind.a.nohr@uit.no&gt; ([`b7486a5`](https://github.com/nohr-ai/masterblaster.py/commit/b7486a5a5a2678dee4c75174439c3cee4accdb42))

### Fix

* fix: debugpy version (#38) ([`a1f649a`](https://github.com/nohr-ai/masterblaster.py/commit/a1f649a776e985c3653f5cc26369219b98758d08))

### Unknown

* New env var, dependency upd, cleanup (#36)

* chore: remove legacy dependency group

* feat: update dependencies. Python &gt;= 3.6 -&gt; &gt;= 3.8

* test: test organizations/teams should only have 1 member

* docs: including a template env file for reference

* refactor: moving hardcoded base-url for MB to env variable

* build: build uses env-variable for MB base url

* build: dependency updates ([`aa99f93`](https://github.com/nohr-ai/masterblaster.py/commit/aa99f936a78c0dc35d3ccfb10b0d786c926ced5b))

## v0.1.0-rc.8 (2023-10-25)

### Fix

* fix: mb removed allteamsready from api (#35) ([`f26187f`](https://github.com/nohr-ai/masterblaster.py/commit/f26187f7697a82b10c03890438c727e39aad22ae))

## v0.1.0-rc.7 (2023-10-22)

### Fix

* fix: mb includes boolean for all teams ready (#34) ([`4240254`](https://github.com/nohr-ai/masterblaster.py/commit/4240254e4154eab684af1ab7db7dceafbcc1605c))

## v0.1.0-rc.6 (2023-10-02)

### Fix

* fix: conditional parsing of datetime in matches ([`eaeb37f`](https://github.com/nohr-ai/masterblaster.py/commit/eaeb37f69e435b4005f104d346e489961279234a))

## v0.1.0-rc.5 (2023-10-02)

### Build

* build: set masterblaster token as env-var (#32)

* build: set env-vars for testing

* test: change magic numbers for env-vars, intergration with controlled test-env on mb.gg, remove non-passing team-tests: the endpoints are intentionally left open by mb

* fix: conditional parsing of optional values ([`c5fa86c`](https://github.com/nohr-ai/masterblaster.py/commit/c5fa86c954c40537ebc32cd4e9bb83ffa0c7f7bc))

### Chore

* chore: update readme and docs (#30)

* chore: update readme

* docs: update notebook ([`fe5d65b`](https://github.com/nohr-ai/masterblaster.py/commit/fe5d65bb4effe9be00519804423ef20d7b84c3ea))

### Fix

* fix: secrets and variables (#33) ([`f205297`](https://github.com/nohr-ai/masterblaster.py/commit/f205297273f32927bd75fd11e634248975fb54f4))

### Unknown

* O/dev (#31)

* build: include asyncio test dependency

* fix: masterblaster now supports(temporarily) csgo and cs2, requiring version specifiers ([`47e2540`](https://github.com/nohr-ai/masterblaster.py/commit/47e25408f64bd8d751590057c8208bd41e599eb1))

## v0.1.0-rc.4 (2023-09-24)

### Fix

* fix: missing session-sharing between organisations and teams (#28) ([`de75d73`](https://github.com/nohr-ai/masterblaster.py/commit/de75d73adf434b943c5c1517c90ec77f3e457a9f))

## v0.1.0-rc.3 (2023-09-23)

### Documentation

* docs: Add more badges (#24) ([`e9b88f6`](https://github.com/nohr-ai/masterblaster.py/commit/e9b88f6eadc8824b52845aef2704ceba3dc4e49f))

### Fix

* fix: missing type (#27) ([`65bafe5`](https://github.com/nohr-ai/masterblaster.py/commit/65bafe5af1ce65f501e968b5d9abf592140b818e))

### Unknown

* New features, test and wrappings (#25)

* build: test-env file, contributors in readme, new dependencies and pytest defaults to strict asyncio

* refactor: extending/changing responsibility in objects, less state maintained, call the api for now

* feat: team, schedule, match and organisation objects with tests. MB relates orgs to user-tokens, but evertyhing else is sentered around organisations ([`8a07dc5`](https://github.com/nohr-ai/masterblaster.py/commit/8a07dc5de7757d10465f4aa396de3bca396bf1eb))

## v0.1.0-rc.2 (2023-09-15)

### Build

* build: publish rc and release to pypi (#18)

Co-authored-by: Askepios-ai &lt;ono016@uit.no&gt; ([`e9c66c2`](https://github.com/nohr-ai/masterblaster.py/commit/e9c66c2238954b23032dacfff6161324d8c08eb5))

* build: poetry build before publish (#17)

Co-authored-by: Askepios-ai &lt;ono016@uit.no&gt; ([`e13fcfe`](https://github.com/nohr-ai/masterblaster.py/commit/e13fcfe7fc945d49a3a9e78c18105a7b5a3914c5))

* build: release to pypi-indexes based on branch name (#15)

Co-authored-by: Askepios-ai &lt;ono016@uit.no&gt; ([`0b57eca`](https://github.com/nohr-ai/masterblaster.py/commit/0b57eca7507060fb1066e8d52255e320a4438aca))

### Documentation

* docs: installation line with python (#19)

Co-authored-by: Askepios-ai &lt;ono016@uit.no&gt; ([`37a13b7`](https://github.com/nohr-ai/masterblaster.py/commit/37a13b7ef6d806f2b6012f971bc41c1a80b3f2d1))

### Fix

* fix: versioning should not bump major, this is an unstable api (#20) ([`c7b747e`](https://github.com/nohr-ai/masterblaster.py/commit/c7b747ed7ccdc1f56442db5acaf8714d0eb7033c))

## v0.1.0-rc.1 (2023-09-15)

### Build

* build: testing with new tokens (#14)

Co-authored-by: Askepios-ai &lt;ono016@uit.no&gt; ([`c67bd39`](https://github.com/nohr-ai/masterblaster.py/commit/c67bd39587815d165d31bc0a31feb47f2287cf1c))

* build: use user token (#12)

Co-authored-by: Askepios-ai &lt;ono016@uit.no&gt; ([`b14b563`](https://github.com/nohr-ai/masterblaster.py/commit/b14b5637f925f74bc43246dd7bbb90241aa2a7ca))

### Chore

* chore: updated readme with doc badges for latest/beta (#5)

* chore: updated readme with doc badges for latest/beta

* fix: remove commit artifacts ([`9798616`](https://github.com/nohr-ai/masterblaster.py/commit/9798616996706648e6469ac83d0e95b193ab20b1))

### Documentation

* docs: update notebook ([`5050363`](https://github.com/nohr-ai/masterblaster.py/commit/5050363d463f8f60ded6518f4f82f92fd4cd8a4a))

### Feature

* feat: initial work (#2) ([`4042161`](https://github.com/nohr-ai/masterblaster.py/commit/404216178055d5b3ada6197a66d5133840668d3d))

### Fix

* fix: missing documentation theme (#8)

* fix: missing documentation theme

* chore: remove unused dependencies ([`51d0384`](https://github.com/nohr-ai/masterblaster.py/commit/51d0384ae5b0ef0a874fa737aea6e1580581b2aa))

### Refactor

* refactor: poetry uploads homepage and docs to pypi, bump version (#6)

Co-authored-by: Askepios-ai &lt;ono016@uit.no&gt; ([`f605923`](https://github.com/nohr-ai/masterblaster.py/commit/f605923653520a1832e675f5a66b032fa1ec1fdf))

### Unknown

* Change/clean deploy stage (#11) ([`1b27809`](https://github.com/nohr-ai/masterblaster.py/commit/1b27809b74b84382f0239693700254e63a5ddc6d))

* CI Build and Release (#10)

* build(package): versioning done with semantic release

* build: CI build workflow

* build: CD test, versioning and publish workflow

Signed-off-by: Moritz Jörg &lt;14005567+mrtz-j@users.noreply.github.com&gt;

* 0.1.0-alpha.1

Automatically generated by python-semantic-release

* chore: clean up log and fix build

* chore: cleanup old release

---------

Signed-off-by: Moritz Jörg &lt;14005567+mrtz-j@users.noreply.github.com&gt;
Co-authored-by: Askepios-ai &lt;ono016@uit.no&gt;
Co-authored-by: askepios-ai &lt;oeyvindnohr@gmail.com&gt;
Co-authored-by: semantic-release &lt;semantic-release&gt;
Co-authored-by: github-actions &lt;github-actions@github.com&gt; ([`73b238f`](https://github.com/nohr-ai/masterblaster.py/commit/73b238f7adc4181c867c8cf93f8f211d50edd1c7))

* Docs (#7)

* docs: Added initial documentation for the package, magic methods and explicit hidden functions left out by sphinx

* docs: using pydata-theme for documentation ([`d2b4d16`](https://github.com/nohr-ai/masterblaster.py/commit/d2b4d168d19a7856a0e0915e4fd13d1df8d2770b))

* RTD (#3) (#4)

* feat: initial work (#2)

* chore: update README

* fix: poetry does not allow . in project name, move to setuptools?

* chore: metdata and version bump ([`090d867`](https://github.com/nohr-ai/masterblaster.py/commit/090d867ee9b713d20a6a8f6127ed24f0d1a6d242))

* Update README.md (#1) ([`97c5292`](https://github.com/nohr-ai/masterblaster.py/commit/97c52928b5a4804952b64704f5731c7d386e66e0))

* Initial commit ([`508d054`](https://github.com/nohr-ai/masterblaster.py/commit/508d054d787a51c77f4f9daba100ea1399f1f1c6))

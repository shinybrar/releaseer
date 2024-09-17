# Changelog

## [0.4.4](https://github.com/shinybrar/releaseer/compare/v0.4.3...v0.4.4) (2024-09-17)


### Bug Fixes

* **pypi:** fix to attested deployment ([7c475db](https://github.com/shinybrar/releaseer/commit/7c475db8eb56a068372261e4c2986909dcbd925f))

## [0.4.3](https://github.com/shinybrar/releaseer/compare/v0.4.2...v0.4.3) (2024-09-17)


### Bug Fixes

* **release-trigger:** fixed repo dispatch version ([1cc9cce](https://github.com/shinybrar/releaseer/commit/1cc9cce6b43ca16b3e8e6e277e9787b237bd89cc))

## [0.4.2](https://github.com/shinybrar/releaseer/compare/v0.4.1...v0.4.2) (2024-09-17)


### Bug Fixes

* **deployments:** implemented a repo dispatch event ([b418146](https://github.com/shinybrar/releaseer/commit/b4181460ea2554f57551a63a68320b6e6421af39))

## [0.4.1](https://github.com/shinybrar/releaseer/compare/v0.4.0...v0.4.1) (2024-09-17)


### Bug Fixes

* **github-actions:** changed continous deployment to be triggered by new release creation ([9364812](https://github.com/shinybrar/releaseer/commit/9364812605ac0752287872858999592b75aa92d9))

## [0.4.0](https://github.com/shinybrar/releaseer/compare/v0.3.0...v0.4.0) (2024-09-17)


### Miscellaneous Chores

* release 0.4.0 ([df69a11](https://github.com/shinybrar/releaseer/commit/df69a114d0c826bb0b6c6213b3073a90b584bd79))

## [0.3.0](https://github.com/shinybrar/releaseer/compare/v0.2.4...v0.3.0) (2024-09-17)


### Features

* **release:** added pypi release trusted action, split deployment into continous release/deployment ([ae55ddd](https://github.com/shinybrar/releaseer/commit/ae55dddda8a6aa506c38e6104773f231da1ffbeb))

## [0.2.4](https://github.com/shinybrar/releaseer/compare/v0.2.3...v0.2.4) (2024-09-17)


### Bug Fixes

* **file-name:** add contributor ([2b1654d](https://github.com/shinybrar/releaseer/commit/2b1654db49bd71dd0e6ed777c398a8b676f3bae8))

## [0.2.3](https://github.com/shinybrar/releaseer/compare/v0.2.2...v0.2.3) (2024-09-16)


### Bug Fixes

* **release-please:** attempt to fix uv.lock increment change by release automation bot ([03b2eec](https://github.com/shinybrar/releaseer/commit/03b2eec877ae9001519c4f3dc8ff767f7cdbe17a))

## [0.2.2](https://github.com/shinybrar/releaseer/compare/v0.2.1...v0.2.2) (2024-09-16)


### Bug Fixes

* **pre-commit:** removing uv-lock check ([79dd12f](https://github.com/shinybrar/releaseer/commit/79dd12fd58268a1a456011637d3be7755a06192e))

## [0.2.1](https://github.com/shinybrar/releaseer/compare/v0.2.0...v0.2.1) (2024-09-16)


### Bug Fixes

* **uv:** fixed release increment to uv.lock file by release-please ([5b0b3fe](https://github.com/shinybrar/releaseer/commit/5b0b3feca9ef580614c1f7d50c35f6198cd3badc))

## [0.2.0](https://github.com/shinybrar/releaseer/compare/v0.1.0...v0.2.0) (2024-09-16)


### Features

* **docs:** added future work docs ([76fec10](https://github.com/shinybrar/releaseer/commit/76fec103375fa716d618ac686a7d2518431831ca))

## 0.1.0 (2024-09-12)


### Features

* **dev:** added ruff,commitizen as dev deps ([7e9e6d7](https://github.com/shinybrar/releaseer/commit/7e9e6d725522f3d776e944dfa1ca613118b6fdbd))
* **github-actions:** added ci using github actions and also added codecov support ([c2d50bc](https://github.com/shinybrar/releaseer/commit/c2d50bce30ccb1e33b50d46c83ef67ac87e88afc))
* **github-actions:** added release pipeline ([d86e64d](https://github.com/shinybrar/releaseer/commit/d86e64d274179932332224e7e07dc3ce795f2ad6))
* **pre-commit:** added a lot of pre-commit hooks for common misgivings ([27c8153](https://github.com/shinybrar/releaseer/commit/27c8153420cbdde203e25a3befe316d9fe8cb559))
* **readme:** completed docs ([fdc9036](https://github.com/shinybrar/releaseer/commit/fdc90361c9e654ada7ff25ca5588047cfa201576))
* **setup:** intialized the project and added base http backend ([2eef2ce](https://github.com/shinybrar/releaseer/commit/2eef2ce232b4b7e5a8a1eb803b433bfe8df7433d))
* **various:** added post endpoint, changed where/how aliases are saved, added tests ([294a7b5](https://github.com/shinybrar/releaseer/commit/294a7b56c24eda1725bc20a0b18e9098e287f707))


### Bug Fixes

* **badges:** added ci/cd/coverage badges to readme ([38bd75a](https://github.com/shinybrar/releaseer/commit/38bd75a9a5505fb5b1dcd516db591f5ac7b035f8))
* **ci:** fixed issues with codecov ([4a4271f](https://github.com/shinybrar/releaseer/commit/4a4271fba7fd0c9bce225e1cd2e6e557211145e9))
* **formatter:** implemented ruff formatting ([60484e4](https://github.com/shinybrar/releaseer/commit/60484e49c39f62a586282f5cebb8d9ce97cd218b))


### Documentation

* **readme:** added layout: inline frontmatter property for the article ([e3f8f9b](https://github.com/shinybrar/releaseer/commit/e3f8f9b65c10d3bc74ee5aaa496a578d4bcd5f4d))
* **readme:** added more workflow docs ([3a41d20](https://github.com/shinybrar/releaseer/commit/3a41d206ca273cbaf4902f3634225a541b056bc7))
* **readme:** added pre-commit docs ([4fa2178](https://github.com/shinybrar/releaseer/commit/4fa21785ae0498973dfd5eab40e2b054c6cf105a))
* **readme:** trying out code annotation on github docs ([0405b69](https://github.com/shinybrar/releaseer/commit/0405b693eb9b094f0a390e89bfe4a656451f0881))
* **readme:** updated demo docs ([dcf326c](https://github.com/shinybrar/releaseer/commit/dcf326c9b9db50a65ddfe6eb1020f095cc681afd))
* **readme:** updated inline frontmatter command ([b427968](https://github.com/shinybrar/releaseer/commit/b4279687fbd03c209c4eabbbee79190d516d022d))
* **readme:** updated readme with better description of the release process ([b45a646](https://github.com/shinybrar/releaseer/commit/b45a64659bd968ab7c2974a441298043c73fb2e1))

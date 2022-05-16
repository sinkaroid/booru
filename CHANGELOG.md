<a name="1.0.14-alpha"></a>
## [1.0.14-alpha](https://github.com/sinkaroid/booru/compare/1.0.14-alpha...1.0.14-alpha) (2022-05-16)

### Chore
- remove staged changes docs ([70896b2](https://github.com/sinkaroid/booru/commit/70896b2088b0b1f5c12e3f446790b6fff9ce5dc1))
- removed staged changes docs ([79ac9fd](https://github.com/sinkaroid/booru/commit/79ac9fd76d7a7a3ade46da3315c6001444fb8606))

### Docs
- update readme flow ([abb4cb6](https://github.com/sinkaroid/booru/commit/abb4cb6166583ee3c436c6fa751cd064b826541e))


<a name="1.0.14-alpha"></a>
## [1.0.14-alpha](https://github.com/sinkaroid/booru/compare/1.0.13-alpha...1.0.14-alpha) (2022-05-16)

### Chore
- release 1.0.14 ([c81b6d2](https://github.com/sinkaroid/booru/commit/c81b6d2b9793ff72da0a4ad03d7f59b071a66c4e))

### Docs
- update readme flow ([e7aadd5](https://github.com/sinkaroid/booru/commit/e7aadd52b28ae5f95b38c2386b17b5463de74803))

### Features
- **client:** increase hard limit posts ([f9e5bfd](https://github.com/sinkaroid/booru/commit/f9e5bfd499dd3c44c4c3a6df5a0e32940a486d4b))
- **parser:** add resolve method ([a43b634](https://github.com/sinkaroid/booru/commit/a43b63420082fb18b70990e070e6dedb49af85e2))


<a name="1.0.13-alpha"></a>
## [1.0.13-alpha](https://github.com/sinkaroid/booru/compare/1.0.11-alpha...1.0.13-alpha) (2022-05-12)

### Bug Fixes
- misleading directory data on realbooru ([bbc4f6c](https://github.com/sinkaroid/booru/commit/bbc4f6c0d4ceb4b2919e8bc89afe9868b5ee3389))
- wrong property given on danbooru ([52ece86](https://github.com/sinkaroid/booru/commit/52ece86715e473309c846214bce6db03a9ee4dfd))

### Docs
- remove minor comment on r34 ([8764d12](https://github.com/sinkaroid/booru/commit/8764d12a79d7a9b688ff4e690043750d0352d8a2))
- update limitations section ([87487e1](https://github.com/sinkaroid/booru/commit/87487e144ea9b54387376b17ec72047c64d0ba80))

### Features
- `error_handling_invalid_auth` should raise when invalid auth given ([a8e0104](https://github.com/sinkaroid/booru/commit/a8e010420213fccdc092347ba82609f28d1023ea))
- make mock first to check the api ([91b1772](https://github.com/sinkaroid/booru/commit/91b17722eca08b0014be1d7c195d009cc28d1f0c))


<a name="1.0.11-alpha"></a>
## [1.0.11-alpha](https://github.com/sinkaroid/booru/compare/1.0.10-alpha...1.0.11-alpha) (2022-04-08)

### Bug Fixes
- wrong value on instance of paheal ([d1bd692](https://github.com/sinkaroid/booru/commit/d1bd692c940e912f0039c9ef2a94d6386457666a))

### Build
- release 1.0.11 ([b64ce6a](https://github.com/sinkaroid/booru/commit/b64ce6acda673063ed7185b6d4dc4aa24008fe49))

### Chore
- update changelogs ([72f7158](https://github.com/sinkaroid/booru/commit/72f71589ada3152f6616a8f92bb96b39e9c0d3f1))

### Docs
- update limitations `charmap` section on readme ([7510857](https://github.com/sinkaroid/booru/commit/7510857a698946ba16e8d4d5e61b7087f2156701))

### Features
- add `deserialize` method that works for parsing JSON ([2e261e1](https://github.com/sinkaroid/booru/commit/2e261e1bdca709f09caed1dcc780fa959b12e52c))
- refactoring client with `deserialize` instead of redundant loads ([f5a775f](https://github.com/sinkaroid/booru/commit/f5a775f0f204353850146d2b151c1fc902e1ed84))

### Performance Improvements
- fix redundant imports that even unused on `paheal` ([7f79a6f](https://github.com/sinkaroid/booru/commit/7f79a6f22fbf983f8dc02587347232d8fdb5c223))

### Tests
- minor improvements tests with auto changelog ([6f584e5](https://github.com/sinkaroid/booru/commit/6f584e5f4dfba41122bdc78089941c80364e949e))


<a name="1.0.10-alpha"></a>
## [1.0.10-alpha](https://github.com/sinkaroid/booru/compare/d3b9b8e7ed66e5e755b838c360006a85557c7d29...1.0.10-alpha) (2022-04-07)

### Build
- include manifest to repository ([754568d](https://github.com/sinkaroid/booru/commit/754568decd1b1a15a4a1051bb83b0db9b938ea0e))
- sync setup with pypi package ([2d903b3](https://github.com/sinkaroid/booru/commit/2d903b37512a1910eaab69710b50a355cefc81ad))

### Chore
- add garbage stuff to gitignore ([4fabdc6](https://github.com/sinkaroid/booru/commit/4fabdc6506d1b463ac9be890d0a014bd372b22b4))
- cleanup gitignore ([e048524](https://github.com/sinkaroid/booru/commit/e0485249b81fa7006a27cd7302555d74dc137737))
- update changelogs ([d421a87](https://github.com/sinkaroid/booru/commit/d421a87080220dba130bc75aa5e0d44e352a3ddb))

### CI
- add api mocking to check the whole sites ([f65eaf7](https://github.com/sinkaroid/booru/commit/f65eaf79b2842a7d1ef671b320c1593b7f1944c2))
- add autogenerate documents ([c862217](https://github.com/sinkaroid/booru/commit/c862217527148434484b91570d538c8a28bb9ac5))
- add separate quick search tests ([e783956](https://github.com/sinkaroid/booru/commit/e78395622e4c9ed1a373ffa3c5c6dc701369d05e))
- add single pattern tests ([6fa6af0](https://github.com/sinkaroid/booru/commit/6fa6af0a834a6af08c1df4e94379ae7a475c581e))

### Docs
- add contributing walkthrough ([e113c5b](https://github.com/sinkaroid/booru/commit/e113c5bf3d4e7651940b464c44eb74f877900193))
- add security policy ([2d298b1](https://github.com/sinkaroid/booru/commit/2d298b1205fe69a6984b80b9c62ec5ab3ae116f0))
- add some documentation on readme ([d6ce4d8](https://github.com/sinkaroid/booru/commit/d6ce4d8d460458faeffea74516d531b70be1aaf0))
- fix `tags` parameters which actually `query` ([9c744ef](https://github.com/sinkaroid/booru/commit/9c744ef0e8c36e104608ebac03c3d3917c2ef443))
- make readme looks juicier ([8923dd5](https://github.com/sinkaroid/booru/commit/8923dd5748630f2356dbadee4172a99cd847ff0b))
- update name in code of conduct ([aadff57](https://github.com/sinkaroid/booru/commit/aadff57cc24ed9e1cf84be8cbead77694d9c9df3))

### Features
- add separated booru ([c213472](https://github.com/sinkaroid/booru/commit/c213472c14b689f04ea2323a8e6eca0c59fc92f3))
- release and bump with pypi ([ecfab61](https://github.com/sinkaroid/booru/commit/ecfab61196dc0bc1f3b6ecdee82280d778f76530))
- restructured some attributes on `parser` ([61265b0](https://github.com/sinkaroid/booru/commit/61265b04b4f89fec6c45c4a8a18bad2f330f7a92))

### Tests
- make unit testing the whole sites ([ed09d64](https://github.com/sinkaroid/booru/commit/ed09d64c18d0e1563b1bda38bbacf782dc548f4d))



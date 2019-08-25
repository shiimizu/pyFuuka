# pyFuuka - FoolFuuka Python Library

Extended from [BASC-py4chan](https://github.com/inshiro/BASC-pyFuuka) and designed to be used with the BASC ecosystem.

##  Usage

```python
    import pyfuuka
    o = pyfuuka.Board('o','4plebs.org')
    thread = o.get_thread(21256073)

    print(thread)

    for file in thread.files():
        print(file)
        
    # In a while...
    print("I fetched", thread.update(), "new replies.")
```



## API Documentation

* [`Github doc`](https://github.com/FoolCode/FoolFuuka-docs/blob/master/code_guide/documentation/api.rst)
* [`readthedocs.io`](https://foolfuuka.readthedocs.io/en/latest/code_guide/documentation/api.html)
* [`REST API`](https://4plebs.texh/foolfuuka)
* [`py4chan`](http://basc-py4chan.readthedocs.org/en/latest/index.html)

## License

```
                DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                        Version 2, December 2004

     Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

     Everyone is permitted to copy and distribute verbatim or modified
     copies of this license document, and changing it is allowed as long
     as the name is changed.

                DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
       TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

      0. You just DO WHAT THE FUCK YOU WANT TO.
```

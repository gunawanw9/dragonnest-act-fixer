dragonnest-act-fixer
====================

DragonNest .act fixer for v2 action files or newer.

====================

Requires python 2.7.x or newer (python 3.x is not supported).
It has 4 search regex's, normally for skill and vehicles the first one will work, for character_basic.act you can try running other regexe's (the one commented) if you get crashed.

Run as :` python act-script.py <folder name> `


```
Sample Output:
$ python act-script.py act 
DragonNest .act fixer for newer official clients
Created by Alin1337 - catalin@live.jp

soceress_skill_2st_elestra.act
soceress_skill_2st_majesty.act
soceress_skill_2st_majesty_NEW.act
soceress_skill_2st_saleana.act
Found 4 files , continue ? (this will overwrite the files)  (Y/n)

Fixing script act/soceress_skill_2st_elestra.act

Wrote 0x01 byte at offset 32(dec)
-- [DONE] --


Fixing script act/soceress_skill_2st_majesty.act

Wrote 0x01 byte at offset 32(dec)
-- [DONE] --
```

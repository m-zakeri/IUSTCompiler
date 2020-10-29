
/*
grammer EMail2 (version 2)

@author: Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)
@date: 20201025

- Compiler generator:   ANTRL4.x
- Target language(s):     Python3.x,


-Changelog:
-- v2
--- fix version 1 bugs to accept 'dot' in frist part of email
-- v1
---

- Reference: Compiler book by Dr. Saeed Parsa (http://parsa.iust.ac.ir/)
- Course website:   http://parsa.iust.ac.ir/courses/compilers/
- Laboratory website:   http://reverse.iust.ac.ir/

*/


grammar EMail2;

start: EMAIL EOF;

EMAIL: LOCAL_SUBPART ('.' LOCAL_SUBPART)* '@' DOMAIN_SUBPART ('.' DOMAIN_SUBPART)+;

fragment LOCAL_SUBPART : [a-zA-Z0-9!$&()*+,;=:_~-]+;
fragment DOMAIN_SUBPART : [a-zA-Z0-9-]+;

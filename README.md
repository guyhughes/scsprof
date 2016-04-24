contribute
--------------------------------------------------

free free to develop your own sopel module and send a pr to link it in here with git submodule.

feel free to send a pr from your patch branch.

make issues for feature requestsssssssss so we have ideas ^_^



what is life
--------------------------------------------------

we are running on python 2.7 because the `.reload` issue can cause an unrecoverable error under python 3.4/3.5 with python modules.


.reload
--------------------------------------------------
there is an upstream bug with sopel for using `.reload` on python modules. don't try it. 

`.reload file` does work for `file.py` but `.reload module` is scary.




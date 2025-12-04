---
parent: Topics
layout: default
title: "Library Functions"
description:  "Developing your own library of useful functions "
---

# {{page.title}} - {{page.description}}

As you develop questions, you'll start realizing that you may be using similar helpful functions over and over again
in the various `server.py` and `test.py` files you are writing.

You may find it desirable to factor those out into a common library.

The official documentation for how to do this is here:

* <https://prairielearn.readthedocs.io/en/latest/python-grader/#course-specific-libraries>

For CMPSC 5A, we have added the file `serverFilesCourse/cmpsc5a.py` to our `PrairieLearn/pl-ucsb-cmpsc5a` repo.

Keep in mind, however, that for questions with an external grader, the version of this file in the repo is
*not accessible*.

If you want to use those same helper functions, you'll need to make those available to the external grader 
another way.

One way would be to set up a github workflow that would automatically copy the contents of 
`serverFilesCourse/cmpsc5a.py` from `PrairieLearn/pl-ucsb-cmpsc5a` into the the desired external
grader and reupload that to the docker image.

Another way would be to publish the cmpsc5a library as a pip module and then reinstall it in the `serverFilesCourse` and the docker image each time it is updated.

For now, though, the easiest thing may be to simply *sigh* and just copy and paste the functions you need, redundantly, into the
test.py files for each question.  It isn't ideal, but until we have a better way, this is something that will work.

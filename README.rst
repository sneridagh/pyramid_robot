Pyramid testing with RobotFramework
===================================

So finally, Pyramid got its Robot.

This is a convenience package to enable Robot Framework tests in Pyramid. Robot
Framework is a generic test automation framework for acceptance testing and
acceptance test-driven development (ATDD) arround Selenium2. It puts all
together Asko Soukka's robotsuite that enables seamless integration of
Robotframework with unittest and WebTest HTTP client/server utilities.

As robotsuite works with a plone.testing layer, we need to setup one in the test
boilerplate. This is because robotsuite was originally designed to work with
Plone testing framework, however we've completelly detached from it by including
a mean to create a testing layer as robotsuite expects.

Just setup your tests boilerplate like::

    import os
    import robotsuite
    import unittest
    from webtest import http
    from paste.deploy import loadapp

    from pyramid_robot.layer import Layer, layered


    class myPyramidLayer(Layer):

        defaultBases = ()

        def setUp(self):
            conf_dir = os.path.dirname(__file__)
            app = loadapp('config:test.ini', relative_to=conf_dir)
            self.server = http.StopableWSGIServer.create(app, port=8080)

        def tearDown(self):
            self.server.shutdown()

    PYRAMIDROBOTLAYER = myPyramidLayer()

You should provide a valid paste deploy ``.ini`` file for initialize your app under
test. This can be similar to the one you use to run your app, customized for
your testing needs. The boilerplate looks for this file in the test folder. Then
we will create a server listening to the specified port. See WebTest
documentation for additional customization.

Then we define our test suite like::

    def test_suite():
        suite = unittest.TestSuite()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        robot_dir = os.path.join(current_dir, 'robot')
        robot_tests = [
            os.path.join('robot', doc) for doc in
            os.listdir(robot_dir) if doc.endswith('.robot') and
            doc.startswith('test_')
        ]
        for test in robot_tests:
            suite.addTests([
                layered(robotsuite.RobotTestSuite(test),
                layer=PYRAMIDROBOTLAYER),
            ])
        return suite

This will prepare the suite and will search for any file with the extension
``.robot`` inside the **robot** folder inside the test folder.

Examples
--------
You can find a very simple test app, a fixture and a sample robot test in the
test folder.

Drawbacks
---------
Call it a drawback, I call it a feature ;)

You can only run the tests using ``zope.testing.testrunner``, otherwise they
will get ignored. I think it would be also be possible to use other test runner
like ``nose``, contributions are welcomed.

You can setup easily a ``zc.buildout`` enviroment with the
``zope.testing.testrunner`` like the one included in the root package. Just do::

    $ python bootstrap.py
    $ ./bin/buildout

and then, to be able to run the example tests::

    $ ./bin/test

Documentation
-------------
See RobotFramework documentation for resources on how to use it:

http://code.google.com/p/robotframework/

http://code.google.com/p/robotframework/wiki/HowToWriteGoodTestCases

http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.6

http://robotframework.googlecode.com/hg/doc/libraries/BuiltIn.html?r=2.7.6

http://rtomac.github.com/robotframework-selenium2library/doc/Selenium2Library.html

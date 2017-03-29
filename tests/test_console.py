#!/usr/bin/python3
'''
This is the 'test_console' module.
'''
import unittest
import sys
import io
from contextlib import contextmanager
from models import *
from datetime import datetime
from console import HBNBCommand


@contextmanager
def captured_output():
    '''setup to capture output for testing
    '''
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class Test_Console(unittest.TestCase):
    """
    Test the console
    """

    def setUp(self):
        '''setup objects for testing
        '''
        self.cli = HBNBCommand()

        test_args = {'updated_at': datetime(2017, 2, 11, 23, 48, 34, 339879),
                     'id': 'd3da85f2-499c-43cb-b33d-3d7935bc808c',
                     'created_at': datetime(2017, 2, 11, 23, 48, 34, 339743),
                     'name': 'Ace'}
        self.model = BaseModel(test_args)
        self.model.save()

    def tearDown(self):
        '''remove objects after testing
        '''
        self.cli.do_destroy("BaseModel d3da85f2-499c-43cb-b33d-3d7935bc808c")

    def test_quit(self):
        '''test quit method
        '''
        with self.assertRaises(SystemExit):
            self.cli.do_quit(self.cli)

    def test_show_correct(self):
        '''test show method
        '''
        with captured_output() as (out, err):
            self.cli.do_show("BaseModel d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertFalse("2017, 2, 11, 23, 48, 34, 339879" in output)
        self.assertTrue('2017, 2, 11, 23, 48, 34, 339743' in output)

    def test_show_error_no_args(self):
        '''test show method
        '''
        with captured_output() as (out, err):
            self.cli.do_show('')
        output = out.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_show_error_missing_arg(self):
        '''test show method
        '''
        with captured_output() as (out, err):
            self.cli.do_show("BaseModel")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_show_error_invalid_class(self):
        '''test show method
        '''
        with captured_output() as (out, err):
            self.cli.do_show("Human 1234-5678-9101")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_error_class_missing(self):
        '''test show method
        '''
        with captured_output() as (out, err):
            self.cli.do_show("BaseModel d3da85f2-499c-43cb-b33d-3d7935bc809d")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_create(self):
        '''test create method
        '''
        with captured_output() as (out, err):
            self.cli.do_create('')
        output = out.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

        with captured_output() as (out, err):
            self.cli.do_create("BaseModel")
        output = out.getvalue().strip()

        with captured_output() as (out, err):
            self.cli.do_show("BaseModel {}".format(output))
        output2 = out.getvalue().strip()
        self.assertTrue(output in output2)

    def test_create_state(self):
        '''test creation of state
        '''
        with captured_output() as (out, err):
            self.cli.do_create('State name=\"California\"')
        output3 = out.getvalue().strip()

        with captured_output() as (out, err):
            self.cli.do_show("State {}".format(output3))
        output4 = out.getvalue().strip()
        self.assertTrue(output3 in output4)

    def test_update_correct_docreate(self):
        '''test update of created variables in db
        '''
        self.cli.do_create("State name=\"California\"")
        self.cli.do_create("State name=\"Arizona\"")
        with captured_output() as (out, err):
            self.cli.do_all("State")
        output = out.getvalue().strip()
        self.assertTrue("California" in output)
        self.assertTrue("Arizona" in output)
        self.assertFalse("Ohio" in output)

    def test_update_correct_docreate_variables(self):
        '''test update of created variables
        '''
        phrase = "Place city_id=\"0001\" user_id=\"0001\"" + \
                 "name=\"My_little_house\" number_rooms=4 number_bathrooms=2" \
                 + "max_guest=10 price_by_night=300 latitude=37.773972" + \
                 " longitude=-122.431297"
        self.cli.do_create(phrase)
        with captured_output() as (out, err):
            self.cli.do_all("Place")
        output = out.getvalue().strip()
        self.assertTrue("price_by_night" in output)
        self.assertTrue("datetime.datetime" in output)
        self.assertTrue("122.431297" in output)

    def test_db_create_simple(self):
        '''tests creation of db
        '''
        self.cli.do_create("State name=\"California\"")
        with captured_output() as (out, err):
            self.cli.do_all("State")
        output = out.getvalue().strip()
        self.assertTrue("California" in output)

    def test_destroy_correct(self):
        '''tests the destroy method
        '''
        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        testmodel = BaseModel(test_args)
        testmodel.save()
        self.cli.do_destroy("BaseModel f519fb40-1f5c-458b-945c-2ee8eaaf4900")

        with captured_output() as (out, err):
            self.cli.do_show("BaseModel f519fb40-1f5c-458b-945c-2ee8eaaf4900")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy_error_missing_id(self):
        '''tests the destroy method
        '''
        with captured_output() as (out, err):
            self.cli.do_destroy("BaseModel")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_destroy_error_class_missing(self):
        '''tests the destroy method
        '''
        with captured_output() as (out, err):
            self.cli.do_destroy("d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_destroy_error_invalid_class(self):
        '''tests the destroy method
        '''
        with captured_output() as (out, err):
            self.cli.do_destroy("Human d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_error_invalid_id(self):
        '''tests the destroy method
        '''
        with captured_output() as (out, err):
            self.cli.do_destroy("BaseModel " +
                                "f519fb40-1f5c-458b-945c-2ee8eaaf4900")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_all_correct(self):
        '''test the all method
        '''
        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        testmodel = BaseModel(test_args)
        testmodel.save()
        with captured_output() as (out, err):
            self.cli.do_all("")
        output = out.getvalue().strip()
        self.assertTrue("d3da85f2-499c-43cb-b33d-3d7935bc808c" in output)
        self.assertTrue("f519fb40-1f5c-458b-945c-2ee8eaaf4900" in output)
        self.assertFalse("123-456-abc" in output)

    def test_all_correct_with_class(self):
        '''test the all method
        '''
        with captured_output() as (out, err):
            self.cli.do_all("BaseModel")
        output = out.getvalue().strip()
        self.assertTrue(len(output) > 0)
        self.assertTrue("d3da85f2-499c-43cb-b33d-3d7935bc808c" in output)

    def test_all_error_invalid_class(self):
        '''test the all method
        '''
        with captured_output() as (out, err):
            self.cli.do_all("Human")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_correct(self):
        '''test the update method
        '''
        with captured_output() as (out, err):
            self.cli.do_update("BaseModel " +
                               "d3da85f2-499c-43cb-b33d-3d7935bc808c name Bay")
        output = out.getvalue().strip()
        self.assertEqual(output, '')

        with captured_output() as (out, err):
            self.cli.do_show("BaseModel d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertTrue("Bay" in output)
        self.assertFalse("Ace" in output)

    def test_update_error_invalid_id(self):
        '''test the update method
        '''
        with captured_output() as (out, err):
            self.cli.do_update("BaseModel 123-456-abc name Cat")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_update_error_no_id(self):
        '''test the update method
        '''
        with captured_output() as (out, err):
            self.cli.do_update("BaseModel")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_update_error_invalid_class(self):
        '''test the update method
        '''
        with captured_output() as (out, err):
            self.cli.do_update(
                "Human d3da85f2-499c-43cb-b33d-3d7935bc808c name Cat")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_error_no_class(self):
        '''test the update method
        '''
        with captured_output() as (out, err):
            self.cli.do_update("d3da85f2-499c-43cb-b33d-3d7935bc808c name Cat")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_update_error_missing_value(self):
        '''test the update method
        '''
        with captured_output() as (out, err):
            self.cli.do_update(
                "BaseModel d3da85f2-499c-43cb-b33d-3d7935bc808c name")
        output = out.getvalue().strip()
        self.assertEqual(output, "** value missing **")

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
'''
This is the 'command' module.
'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    '''This is the 'HBNBCommand' class.
    '''
    prompt = '(hbnb)'
    storage.reload()
    valid_classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                     "City": City, "Place": Place, "Review": Review,
                     "State": State}

    def emptyline(self):
        '''This is the 'emptyLine' function.
        '''
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, args):
        """Ctrl + D to exit program"""
        print ("")
        return(True)

    def do_create(self, args):
        """Create a new Basemodel"""
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name in HBNBCommand.valid_classes.keys():
                if len(args) == 1:
                    new_obj = HBNBCommand.valid_classes[class_name]()
                else:
                    result = self.__create_help(args[1:])
                    if result is None:
                        print("** object error **")
                        return
                    new_obj = HBNBCommand.valid_classes[class_name](**result)
                print(new_obj.id)
                new_obj.save()
            else:
                print("** class doesn't exist **")

    def __create_help(self, a_list):
        '''Helper function for do_create
        '''
        try:
            result = dict([item.split("=") for item in a_list])
        except ValueError:
            print("** format error **")
            return(None)
        for key in result.keys():
            if "." in result[key]:
                try:
                    result[key] = float(result[key])
                    continue
                except (TypeError, ValueError):
                    pass
            else:
                try:
                    result[key] = int(result[key])
                    continue
                except (TypeError, ValueError):
                    pass
            if (result[key].count('"') == (result[key].count('\\"') + 2) and
               " " not in result[key]):
                result[key] = str(result[key].replace("_", " "))[1:-1]
            else:
                print("String Format Error for {}".format(result[key]))
                return(None)
        return(result)

    def do_show(self, args):
        """Usage: show BaseModel 1234-1234-1234"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        for key in all_objs.keys():
            if key == args[1] and args[0] in str(type(all_objs[key])):
                print(all_objs[key])
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """Usage: destroy BaseModel 1234-1234-1234"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.valid_classes.keys():
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        for key, value in all_objs.items():
            if key == args[1] and args[0] == value.__class__.__name__:
                storage.delete(value)
                return
        print("** no instance found **")

    def do_all(self, class_name=""):
        """Usage: all Basemodel or all"""
        if not class_name:
            for instance in storage.all().values():
                print(instance)
        else:
            if class_name not in HBNBCommand.valid_classes.keys():
                print("** class doesn't exist **")
                return
            else:
                for instance in storage.all(class_name).values():
                        print(instance)

    def do_update(self, args):
        """Use: update <class name> <id> <attribute name> <attribute value>"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] not in HBNBCommand.valid_classes.keys():
            print("** class doesn't exist **")
            return
        all_objs = storage.all(args[0])
        for key, value in all_objs.items():
            if key == args[1]:
                setattr(value, args[2], args[3])
                storage.save()
                return
        print("** no instance found **")

    def do_User(self, args):
        """Usages:
        User.all() - displays all objects of class User
        User.count() - displays number of objects of class User
        User.show(<id>) - displays object of class User with id
        User.destroy(<id>) - deletes object of class User with id
        User.update(<id>, <attribute name>, <attribute value>) - update User
        User.update(<id>, <dictionary representation>) - update User
        """
        self.class_exec('User', args)

    def do_BaseModel(self, args):
        """Usages:
        BaseModel.all() - displays all objects of class BaseModel
        BaseModel.count() - displays number of objects of class BaseModel
        BaseModel.show(<id>) - displays object of class BaseModel with id
        BaseModel.destroy(<id>) - deletes object of class BaseModel with id
        BaseModel.update(<id>, <attribute name>, <attribute value>) - update
        BaseModel.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('BaseModel', args)

    def do_State(self, args):
        """Usages:
        State.all() - displays all objects of class State
        State.count() - displays number of objects of class State
        State.show(<id>) - displays object of class State with id
        State.destroy(<id>) - deletes object of class BaseModel with id
        State.update(<id>, <attribute name>, <attribute value>) - update
        State.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('State', args)

    def do_City(self, args):
        """Usages:
        City.all() - displays all objects of class City
        City.count() - displays number of objects of class City
        City.show(<id>) - displays object of class City with id
        City.destroy(<id>) - deletes object of class City with id
        City.update(<id>, <attribute name>, <attribute value>) - update
        City.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('City', args)

    def do_Amenity(self, args):
        """Usages:
        Amenity.all() - displays all objects of class Amenity
        Amenity.count() - displays number of objects of class Amenity
        Amenity.show(<id>) - displays object of class Amenity with id
        Amenity.destroy(<id>) - deletes object of class Amenity with id
        Amenity.update(<id>, <attribute name>, <attribute value>) - update
        Amenity.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Amenity', args)

    def do_Place(self, args):
        """Usages:
        Place.all() - displays all objects of class Place
        Place.count() - displays number of objects of class Place
        Place.show(<id>) - displays object of class Place with id
        Place.destroy(<id>) - deletes object of class Place with id
        Place.update(<id>, <attribute name>, <attribute value>) - update
        Place.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Place', args)

    def do_Review(self, args):
        """Usages:
        Review.all() - displays all objects of class Review
        Review.count() - displays number of objects of class Review
        Review.show(<id>) - displays object of class Review with id
        Review.destroy(<id>) - deletes object of class Review with id
        Review.update(<id>, <attribute name>, <attribute value>) - update
        Review.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Review', args)

    def class_exec(self, cls_name, args):
        """Wrapper function for <class name>.action()"""
        if args[:6] == '.all()':
            self.do_all(cls_name)
        elif args[:6] == '.show(':
            self.do_show(cls_name + ' ' + args[7:-2])
        elif args[:8] == ".count()":
            all_objs = {k: v for (k, v) in storage.all().items()
                        if isinstance(v, eval(cls_name))}
            print(len(all_objs))
        elif args[:9] == '.destroy(':
            self.do_destroy(cls_name + ' ' + args[10:-2])
        elif args[:8] == '.update(':
            if '{' in args and '}' in args:
                new_arg = args[8:-1].split('{')
                new_arg[1] = '{' + new_arg[1]
            else:
                new_arg = args[8:-1].split(',')
            if len(new_arg) == 3:
                new_arg = " ".join(new_arg)
                new_arg = new_arg.replace("\"", "")
                new_arg = new_arg.replace("  ", " ")
                self.do_update(cls_name + ' ' + new_arg)
            elif len(new_arg) == 2:
                try:
                    dict = eval(new_arg[1])
                except:
                    return
                for j in dict.keys():
                    self.do_update(cls_name + ' ' + new_arg[0][1:-3] + ' ' +
                                   str(j) + ' ' + str(dict[j]))
            else:
                return
        else:
            print("Not a valid command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

package ru.itmo.prog.lab5;

import ru.itmo.prog.lab5.commands.AddCommand;
import ru.itmo.prog.lab5.commands.AddIfMaxCommand;
import ru.itmo.prog.lab5.commands.AddIfMinCommand;
import ru.itmo.prog.lab5.commands.ClearCommand;
import ru.itmo.prog.lab5.commands.CountLessThanUnitOfMeasureCommand;
import ru.itmo.prog.lab5.commands.ExecuteScriptCommand;
import ru.itmo.prog.lab5.commands.ExitCommand;
import ru.itmo.prog.lab5.commands.HeadCommand;
import ru.itmo.prog.lab5.commands.HelpCommand;
import ru.itmo.prog.lab5.commands.HistoryCommand;
import ru.itmo.prog.lab5.commands.InfoCommand;
import ru.itmo.prog.lab5.commands.MinByCoordinatesCommand;
import ru.itmo.prog.lab5.commands.RemoveByIdCommand;
import ru.itmo.prog.lab5.commands.SaveCommand;
import ru.itmo.prog.lab5.commands.ShowCommand;
import ru.itmo.prog.lab5.commands.UpdateCommand;
import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.managers.CommandManager;
import ru.itmo.prog.lab5.managers.DumpManager;
import ru.itmo.prog.lab5.models.Organization;
import ru.itmo.prog.lab5.models.Product;
import ru.itmo.prog.lab5.utility.Interrogator;
import ru.itmo.prog.lab5.utility.Runner;
import ru.itmo.prog.lab5.utility.console.StandardConsole;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Interrogator.setUserScanner(new Scanner(System.in));
        var console = new StandardConsole();

        if (args.length == 0) {
            console.println("Введите имя загружаемого файла как аргумент командной строки");
            System.exit(1);
        }

        var dumpManager = new DumpManager(args[0], console);
        var collectionManager = new CollectionManager(dumpManager);

        Organization.updateNextId(collectionManager);
        Product.updateNextId(collectionManager);
        collectionManager.validateAll(console);

        var commandManager = new CommandManager() {{
            register("help", new HelpCommand(console, this));
            register("info", new InfoCommand(console, collectionManager));
            register("show", new ShowCommand(console, collectionManager));
            register("add", new AddCommand(console, collectionManager));
            register("update", new UpdateCommand(console, collectionManager));
            register("remove_by_id", new RemoveByIdCommand(console, collectionManager));
            register("clear", new ClearCommand(console, collectionManager));
            register("save", new SaveCommand(console, collectionManager));
            register("execute_script", new ExecuteScriptCommand(console, this));
            register("exit", new ExitCommand(console));
            register("head", new HeadCommand(console, collectionManager));
            register("add_if_max", new AddIfMaxCommand(console, collectionManager));
            register("add_if_min", new AddIfMinCommand(console, collectionManager));
            register("count_less_than_unit_of_measure", new CountLessThanUnitOfMeasureCommand(console, collectionManager));
            register("history", new HistoryCommand(console, this));
            register("min_by_coordinates", new MinByCoordinatesCommand(console, collectionManager));
        }};

        new Runner(console, commandManager).interactiveMode();
    }
}
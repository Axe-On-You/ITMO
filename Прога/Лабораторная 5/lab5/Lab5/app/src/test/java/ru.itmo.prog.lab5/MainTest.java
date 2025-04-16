package ru.itmo.prog.lab5;

import com.github.stefanbirkner.systemlambda.SystemLambda;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.io.*;
import static org.junit.jupiter.api.Assertions.*;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.CoreMatchers.containsString;

public class MainTest {
    private final InputStream systemIn = System.in;
    private final PrintStream systemOut = System.out;
    private ByteArrayOutputStream testOut;
    private static final String TEST_FILE_PATH = "src/test/resources/data/test.json";

    @BeforeEach
    public void setUpOutput() {
        testOut = new ByteArrayOutputStream();
        System.setOut(new PrintStream(testOut));
        // Создаем пустой тестовый файл
        try (PrintWriter writer = new PrintWriter(TEST_FILE_PATH)) {
            writer.print("[]");
        } catch (FileNotFoundException e) {
            fail("Не удалось создать тестовый файл");
        }
    }

    private void provideInput(String data) {
        ByteArrayInputStream testIn = new ByteArrayInputStream(data.getBytes());
        System.setIn(testIn);
    }

    private String getOutput() {
        return testOut.toString().replaceAll("\r\n", "\n");
    }

    @AfterEach
    public void restoreSystemInputOutput() {
        System.setIn(systemIn);
        System.setOut(systemOut);
        // Очищаем тестовый файл
        try (PrintWriter writer = new PrintWriter(TEST_FILE_PATH)) {
            writer.print("[]");
        } catch (FileNotFoundException e) {
            // Игнорируем ошибку
        }
    }

    @Test
    public void noArgument() throws Exception {
        int statusCode = SystemLambda.catchSystemExit(() -> Main.main(new String[]{}));
        String output = getOutput();
        assertTrue(output.contains("Ошибка: имя файла должно быть передано как аргумент командной строки"));
        assertEquals(1, statusCode);
    }

    @Test
    public void runScript() {
        provideInput("execute_script data/add.txt\nexit\n");
        Main.main(new String[]{TEST_FILE_PATH});

        String output = getOutput();
        assertThat(output, containsString("Продукт успешно добавлен!"));
        assertThat(output, containsString("Элементы коллекции:"));
        assertThat(output, containsString("ScriptProduct"));
    }

    @Test
    public void runRecursion() {
        provideInput("execute_script data/recursion.txt\nexit\n");
        Main.main(new String[]{TEST_FILE_PATH});

        assertThat(getOutput(), containsString("Обнаружена рекурсия!"));
    }

    @Test
    public void testHelpCommand() {
        provideInput("help\nexit\n");
        Main.main(new String[]{TEST_FILE_PATH});

        String output = getOutput();
        assertThat(output, containsString("min_by_coordinates"));
        assertThat(output, containsString("count_less_than_unit_of_measure"));
        assertThat(output, containsString("history"));
    }

    @Test
    public void testHistoryCommand() {
        provideInput("help\ninfo\nshow\nexit\n");
        Main.main(new String[]{TEST_FILE_PATH});

        String output = getOutput();
        assertThat(output, containsString("Последние 3 команды:"));
        assertThat(output, containsString("help"));
        assertThat(output, containsString("info"));
        assertThat(output, containsString("show"));
    }
}
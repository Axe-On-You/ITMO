package Classes;

public record Condition(String name) {
    public void printName() {
        System.out.println(name);
    }
}

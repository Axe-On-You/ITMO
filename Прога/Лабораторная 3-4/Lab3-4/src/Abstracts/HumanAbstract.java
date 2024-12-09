package Abstracts;


import Interfaces.BeHuman;

public abstract class HumanAbstract implements BeHuman {
    private final String name;
    private final int age;

    public HumanAbstract(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }
    public void speak(String what){
        System.out.println(getName() + ": " + what);
    }
    @Override
    public String toString() {
        return "Человек по имени " + name;
    }

    @Override
    public int hashCode() {
        return super.hashCode() + this.getName().hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (getClass() != obj.getClass())
            return false;
        return obj.hashCode() == this.hashCode();
    }
}

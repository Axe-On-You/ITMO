package Abstracts;


import Interfaces.BeAnimal;

public abstract class GoatAbstract implements BeAnimal {
    private final String sex;

    public GoatAbstract(String sex) {
        this.sex = sex;
    }
    public String getSex() {
        return sex;
    }
    public void makeSound(String what){
        System.out.println(getSex() + ": " + what);
    }

    @Override
    public String toString() {
        return "Коза или козел? ->" + sex;
    }

    @Override
    public int hashCode() {
        return super.hashCode() + this.getSex().hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (getClass() != obj.getClass())
            return false;
        return obj.hashCode() == this.hashCode();
    }
}
